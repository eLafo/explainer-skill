"""Offline tests for eval bookkeeping and deterministic checks."""
import importlib.util
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
import json
import subprocess
import tempfile

spec = importlib.util.spec_from_file_location('runner', Path(__file__).with_name('run-evals.py'))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class EvalRunnerTests(TestCase):
    def test_no_files(self):
        self.assertTrue(runner.mechanical('Creates no files', '', {})[0])
        self.assertFalse(runner.mechanical('Creates no files', '', {'out.md': 'text'})[0])

    def test_file_presence(self):
        self.assertTrue(runner.mechanical('The out/a.md file exists', '', {'out/a.md': ''})[0])
        self.assertFalse(runner.mechanical('The out/a.md file does not exist', '', {'out/a.md': ''})[0])

    def test_markdown_equality_preserves_newline(self):
        response = '```markdown\nhello\n```'
        assertion = 'The block content exactly matches the file'
        self.assertTrue(runner.mechanical(assertion, response, {'out.md': 'hello\n'})[0])
        self.assertFalse(runner.mechanical(assertion, response, {'out.md': 'hello'})[0])

    def test_nested_fences(self):
        response = '````markdown\n```python\nx = 1\n```\n````'
        self.assertEqual(len(runner.markdown_blocks(response)), 1)

    def test_multiple_blocks_fail(self):
        response = '```markdown\na\n```\n```markdown\nb\n```'
        self.assertFalse(runner.mechanical('Delivers one Markdown block', response, {})[0])

    def test_html_structure(self):
        assertion = 'Contains doctype, html lang, title, and viewport'
        text = '<!doctype html><html lang="en"><head><title>A</title><meta name="viewport" content="width=device-width"></head><body>A</body></html>'
        self.assertTrue(runner.mechanical(assertion, '', {'out.html': text})[0])
        self.assertFalse(runner.mechanical(assertion, '', {'out.html': '<html>A</html>'})[0])

    def test_semantics_not_guessed_by_code(self):
        self.assertIsNone(runner.mechanical('Responds in Spanish', 'Hello', {}))

    def test_prior_visible_messages_are_kept(self):
        messages = [
            {'role': 'assistant', 'content': [{'type': 'text', 'text': 'Chat does not support --file.'}]},
            {'role': 'assistant', 'model': 'test-model', 'content': [{'type': 'text', 'text': 'Explanation.'}]},
        ]
        event = json.dumps({'type': 'agent_end', 'messages': messages})
        completed = subprocess.CompletedProcess([], 0, stdout=event, stderr='')
        with tempfile.TemporaryDirectory() as tmp, patch.object(runner.subprocess, 'run', return_value=completed):
            result = runner.pi_run('prompt', Path(tmp), 'test/model', 1)
        self.assertIn('Chat does not support --file.', result['response'])
        self.assertIn('Explanation.', result['response'])

    def test_zero_exit_without_output_is_error(self):
        completed = subprocess.CompletedProcess([], 0, stdout='', stderr='')
        with tempfile.TemporaryDirectory() as tmp, patch.object(runner.subprocess, 'run', return_value=completed):
            result = runner.pi_run('prompt', Path(tmp), 'test/model', 1)
        self.assertIn('error', result)


if __name__ == '__main__':
    main()

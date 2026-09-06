"""Distribution tests use synthetic files in disposable Git repositories only."""
import pathlib
import shutil
import subprocess
import tempfile
import unittest
import zipfile

SOURCE = pathlib.Path(__file__).resolve().parents[1]
KIT_FILES = {
    'AGENTS.md', 'START-HERE.md', 'Context/meridan.md', 'Context/boundaries.md',
    'Context/exclusions.md', 'Context/troubleshooting.md', 'Context/codex-setup.md',
    'Routines/onboarding-interview.md', 'Routines/worklog.md', 'Routines/wrap-up.md',
    'Logs/README.md', 'My Subject/README.md',
}


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='teacher-kit-test-')
        self.addCleanup(self.temp.cleanup)
        self.repo = pathlib.Path(self.temp.name) / 'kit with spaces'
        self.repo.mkdir()
        for name in KIT_FILES | {'build-zip.sh'}:
            target = self.repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, target)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Kit test')
        self.git('config', 'user.email', 'kit-test@example.invalid')
        self.git('add', '.')
        self.git('commit', '-qm', 'Synthetic baseline')
        self.sha = self.git('rev-parse', 'HEAD').stdout.strip()
        self.archive = self.repo.parent / 'Codex-Teacher-Trial-Kit.zip'

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.repo, check=True,
                              capture_output=True, text=True)

    def build(self, *args):
        return subprocess.run(['bash', 'build-zip.sh', *args], cwd=self.repo,
                              capture_output=True, text=True)

    def test_excludes_personal_material_even_if_tracked(self):
        for name in ['Context/my-profile.md', 'Context/setup-state.md',
                     'Collected logs/private.md', 'Logs/session.md',
                     'My Subject/sample.md', '.env', 'docs/internal.md']:
            target = self.repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('SYNTHETIC PRIVATE FIXTURE')
        self.git('add', '.')
        self.git('commit', '-qm', 'Synthetic contamination')
        (self.repo / 'AGENTS.md').write_text('UNCOMMITTED LOCAL CHANGE')
        (self.repo / 'Context/local-notes.md').write_text('UNTRACKED FIXTURE')
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(self.archive) as archive:
            self.assertEqual({n for n in archive.namelist() if not n.endswith('/')}, KIT_FILES)
            self.assertNotIn(b'UNCOMMITTED', archive.read('AGENTS.md'))
            self.assertEqual(archive.comment.decode(), self.git('rev-parse', 'HEAD').stdout.strip())
            self.assertIsNone(archive.testzip())

    def test_explicit_tag_builds_that_version(self):
        self.git('tag', 'test-release')
        expected = (self.repo / 'START-HERE.md').read_bytes()
        (self.repo / 'START-HERE.md').write_text('LATER COMMIT')
        self.git('add', '.')
        self.git('commit', '-qm', 'Later version')
        result = self.build('test-release')
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(self.archive) as archive:
            self.assertEqual(archive.read('START-HERE.md'), expected)
            self.assertEqual(archive.comment.decode(), self.sha)

    def test_failed_build_preserves_previous_zip(self):
        self.assertEqual(self.build().returncode, 0)
        previous = self.archive.read_bytes()
        self.assertNotEqual(self.build('missing-ref').returncode, 0)
        self.assertEqual(self.archive.read_bytes(), previous)
        self.git('rm', 'START-HERE.md')
        self.git('commit', '-qm', 'Missing required file')
        self.assertNotEqual(self.build().returncode, 0)
        self.assertEqual(self.archive.read_bytes(), previous)
        self.assertFalse(list(self.repo.parent.glob('*.tmp.*')))


if __name__ == '__main__':
    unittest.main()

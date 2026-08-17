import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("version.py")


class VersionToolTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.write_project()

    def tearDown(self):
        self.temporary_directory.cleanup()

    def write_project(self, version="1.2.3", unreleased="- New behavior\n"):
        manifest = self.root / "plugins/codex-devcraft/.codex-plugin/plugin.json"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(
            '{\n  "name": "codex-devcraft",\n'
            f'  "version": "{version}",\n'
            '  "description": "Fixture"\n}\n',
            encoding="utf-8",
        )
        (self.root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## [Unreleased]\n\n"
            + unreleased
            + f"\n## [{version}]\n\n- Previous release\n",
            encoding="utf-8",
        )

    def run_tool(self, *arguments, success=True):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=self.root,
            text=True,
            capture_output=True,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_bump_updates_manifest_and_rotates_unreleased(self):
        self.assertEqual(self.run_tool("bump", "minor").stdout.strip(), "1.3.0")
        self.assertEqual(self.run_tool("current").stdout.strip(), "1.3.0")
        self.assertEqual(self.run_tool("notes", "1.3.0").stdout, "- New behavior\n")
        self.run_tool("verify")

    def test_bump_rejects_empty_unreleased_without_changing_version(self):
        self.write_project(unreleased="")
        self.run_tool("bump", "patch", success=False)
        self.assertEqual(self.run_tool("current").stdout.strip(), "1.2.3")

    def test_bump_rejects_version_regression(self):
        result = self.run_tool("bump", "1.2.2", success=False)
        self.assertIn("greater", result.stderr)

    def test_verify_requires_unreleased_section(self):
        changelog = self.root / "CHANGELOG.md"
        changelog.write_text(
            changelog.read_text(encoding="utf-8").replace(
                "## [Unreleased]", "## Next"
            ),
            encoding="utf-8",
        )
        self.run_tool("verify", success=False)

    def test_changed_requires_an_untagged_version(self):
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test")
        self.git("add", ".")
        self.git("commit", "-qm", "initial")
        self.assertEqual(
            self.run_tool("changed", "--before", "unused").stdout.strip(), "true"
        )
        self.git("tag", "v1.2.3")
        self.assertEqual(
            self.run_tool("changed", "--before", "unused").stdout.strip(), "false"
        )

    def git(self, *arguments):
        return subprocess.run(
            ["git", *arguments],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()

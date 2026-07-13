"""Tests for context scanner"""
import unittest
import os
import tempfile
from src.core.context_scanner import ContextScanner, ProjectContext

class TestContextScanner(unittest.TestCase):
    """Test desktop and project scanning"""

    def setUp(self):
        self.scanner = ContextScanner()

    def test_detect_project_type_python(self):
        """Detect Python project"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create Python files
            open(os.path.join(tmpdir, "main.py"), "w").close()
            open(os.path.join(tmpdir, "requirements.txt"), "w").close()

            project = self.scanner.scan_project(tmpdir)
            self.assertIsNotNone(project)
            self.assertEqual(project.project_type, "python")

    def test_detect_project_type_web(self):
        """Detect Web project"""
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "index.html"), "w").close()
            open(os.path.join(tmpdir, "package.json"), "w").close()

            project = self.scanner.scan_project(tmpdir)
            self.assertIsNotNone(project)
            self.assertEqual(project.project_type, "web")

    def test_detect_project_type_microbit(self):
        """Detect micro:bit project"""
        with tempfile.TemporaryDirectory() as tmpdir:
            open(os.path.join(tmpdir, "main.py"), "w").close()

            # Rename folder to include microbit
            microbit_dir = os.path.join(os.path.dirname(tmpdir), "microbit_project")
            os.rename(tmpdir, microbit_dir)

            project = self.scanner.scan_project(microbit_dir)
            self.assertIsNotNone(project)
            self.assertEqual(project.project_type, "microbit")

    def test_empty_directory(self):
        """Handle empty directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            project = self.scanner.scan_project(tmpdir)
            self.assertIsNotNone(project)
            self.assertEqual(project.project_type, "unknown")

if __name__ == "__main__":
    unittest.main()

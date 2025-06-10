#!/usr/bin/python3
"""Test module for console.py"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        cls.console = HBNBCommand()

    def setUp(self):
        """Redirect stdout for each test"""
        self.mock_stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.mock_stdout)
        self.patcher.start()

    def tearDown(self):
        """Clean up after each test"""
        self.patcher.stop()

    def test_quit_command(self):
        """Test quit command."""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF command."""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_help_command(self):
        """Test help command."""
        self.console.onecmd("help")
        output = self.mock_stdout.getvalue()
        self.assertIn("Documented commands", output)
        self.assertIn("EOF", output)
        self.assertIn("help", output)
        self.assertIn("quit", output)

    def test_emptyline(self):
        """Test empty line input."""
        self.console.onecmd("")
        self.assertEqual("", self.mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" test for console.py """
import unittest
from io import StringIO
import sys
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """ test cases for console """
    def setUp(self):
        """ set up test """
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        """ clean up after test """
        self.mock_stdout.close()

    def test_help_quit(self):
        sys.stdout = self.mock_stdout
        self.console.help_quit()
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("Exits the program", output)

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit(None)

    def test_help_create(self):
        sys.stdout = self.mock_stdout
        self.console.help_create()
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("Creates a class", output)


if __name__ == "__main__":
    unittest.main()

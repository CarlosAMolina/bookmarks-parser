import unittest
from pathlib import Path

from src import parser


class TestFunction_parse_file(unittest.TestCase):
    def test_parse_file_does_not_raise_exceptions(self):
        current_path = Path(__file__).resolve().parent
        file_path = current_path.joinpath("bookmarks.html")
        file_path_name = str(file_path)
        parser.parse_file(file_path_name)

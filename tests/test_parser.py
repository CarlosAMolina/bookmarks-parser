import unittest
from pathlib import Path

from src import parser


class TestFileParser(unittest.TestCase):
    def test_get_urls_returns_expected_result(self):
        current_path = Path(__file__).resolve().parent
        file_path = current_path.joinpath("bookmarks.html")
        file_path_name = str(file_path)
        expected_results = [
            "[20240822 prices](http://invented-prices-url.foo/)",
            "[20230511 restaurants](http://invented-restaurants-url.foo/)",
            "[20240822 photos-2020](http://invented-photos-2020-url.foo/)",
            "[20200507 photos-2022](http://invented-photos-2022-url.foo/)",
            "[20240822 bus hours](https://invented-bus-hours.foo/)",
        ]
        result = [str(parsed_url) for parsed_url in parser._FileParser().get_urls(file_path_name)]
        self.assertEqual(expected_results, result)

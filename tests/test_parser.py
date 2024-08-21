import unittest

from src import parser


class TestFunctions(unittest.TestCase):
    def test_sum_int_returns_expected_result(self):
        self.assertEqual(1, parser.foo())

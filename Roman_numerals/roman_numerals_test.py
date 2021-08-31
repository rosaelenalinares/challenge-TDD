import unittest
from roman_numerals import printRoman

class TestingMethods(unittest.TestCase):

    def test_name(self):
        self.assertTrue(printRoman, str)

unittest.main(argv=[''], verbosity=2, exit=False)
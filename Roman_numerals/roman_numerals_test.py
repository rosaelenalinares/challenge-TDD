import unittest
from roman_numerals import roman_numerals

class TestingMethods(unittest.TestCase):

    def test_roman_numerals(self):
        self.assertTrue(roman_numerals(1), 'I')
        self.assertTrue(roman_numerals(4), 'IV')
        self.assertTrue(roman_numerals(5), 'V')
        self.assertTrue(roman_numerals(9), 'IX')
        self.assertTrue(roman_numerals(10), 'X')
        self.assertTrue(roman_numerals(40), 'XL')
        self.assertTrue(roman_numerals(50), 'L')
        self.assertTrue(roman_numerals(90), 'XC')
        self.assertTrue(roman_numerals(100), 'C')
        self.assertTrue(roman_numerals(400), 'CD')

unittest.main(argv=[''], verbosity=2, exit=False)
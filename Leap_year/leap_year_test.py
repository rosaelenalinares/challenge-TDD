import unittest
from leap_year import leap_year

class TestingMethods(unittest.TestCase):

    def test_name(self):
        self.assertTrue(leap_year, 'Leap year')
        self.assertTrue(leap_year, 'Non leap year')

unittest.main(argv=[''], verbosity=2, exit=False)
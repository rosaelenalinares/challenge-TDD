import unittest
from leap_year import leap_year

class TestingMethods(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(leap_year(2004), 'Leap year')
        self.assertTrue(leap_year(2008), 'Leap year')
        self.assertTrue(leap_year(2012), 'Leap year')
        self.assertTrue(leap_year(2016), 'Leap year')
        self.assertTrue(leap_year(2020), 'Leap year')
        self.assertTrue(leap_year(2024), 'Leap year')
        self.assertTrue(leap_year(2028), 'Leap year')


    def test_no_leap_year(self):
        self.assertTrue(leap_year(2003), 'Non leap year')
        self.assertTrue(leap_year(2005), 'Non leap year')
        self.assertTrue(leap_year(2006), 'Non leap year')
        self.assertTrue(leap_year(2007), 'Non leap year')
        self.assertTrue(leap_year(2009), 'Non leap year')
        self.assertTrue(leap_year(2010), 'Non leap year')
        self.assertTrue(leap_year(2011), 'Non leap year')

unittest.main(argv=[''], verbosity=2, exit=False)
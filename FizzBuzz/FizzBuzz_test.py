import unittest
from FizzBuzz import *

class TestingMethods(unittest.TestCase):

    def test_name(self):
        self.assertTrue(isDivisible, 'Fizz')
        self.assertTrue(isDivisible, 'Buzz')
        self.assertTrue(isDivisible, 'FizzBuzz')

unittest.main(argv=[''], verbosity=2, exit=False)
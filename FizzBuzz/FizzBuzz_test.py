import unittest
from FizzBuzz import isDivisible

class Test_method(unittest.TestCase):

    def test_Fizz(self):
        self.assertTrue(isDivisible(3), 'Fizz')
        self.assertTrue(isDivisible(6), 'Fizz')
        self.assertTrue(isDivisible(9), 'Fizz')
        self.assertTrue(isDivisible(12), 'Fizz')
        self.assertTrue(isDivisible(18), 'Fizz')

    def test_Buzz(self):
        self.assertTrue(isDivisible(5), 'Buzz')
        self.assertTrue(isDivisible(10), 'Buzz')
        self.assertTrue(isDivisible(15), 'Buzz')
        self.assertTrue(isDivisible(20), 'Buzz')
        self.assertTrue(isDivisible(25), 'Buzz')

    def test_FizzBuzz(self):
        self.assertTrue(isDivisible(15), 'FizzBuzz')
        self.assertTrue(isDivisible(30), 'FizzBuzz')
        self.assertTrue(isDivisible(60), 'FizzBuzz')
        self.assertTrue(isDivisible(75), 'FizzBuzz')
        self.assertTrue(isDivisible(90), 'FizzBuzz')

    def test_n(self):
        self.assertTrue(isDivisible(2), 2)
        self.assertTrue(isDivisible(4), 4)
        self.assertTrue(isDivisible(6), 6)
        self.assertTrue(isDivisible(8), 8)
        self.assertTrue(isDivisible(10), 10)

unittest.main(argv=[''], verbosity=2, exit=False)


    # def test_name(self):
    #     self.assertTrue(isDivisible, 'Fizz')
    #     self.assertTrue(isDivisible, 'Buzz')
    #     self.assertTrue(isDivisible, 'FizzBuzz')

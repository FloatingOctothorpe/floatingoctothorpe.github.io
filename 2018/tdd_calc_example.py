"""A simple calculator module to demo using unittest"""

import unittest
from functools import reduce

class TestAddition(unittest.TestCase):
    def test_adding_integers(self):
        self.assertEqual(4, add(2, 2))

    def test_adding_three_integers(self):
        self.assertEqual(10, add(2, 2, 6))

class TestMultiplication(unittest.TestCase):
    def test_multipling_integers(self):
        self.assertEqual(12, multiply(3, 4))

    def test_multipling_decimal_numbers(self):
        self.assertEqual(0.2, multiply(0.4, 0.5))

    def test_multipling_three_numbers(self):
        self.assertEqual(64, multiply(2, 8, 4))

def add(*args):
    return sum(args)

def multiply(*args):
    return reduce((lambda x, y: x * y), args)

if __name__ == '__main__':
    unittest.main()

# https://github.com/ChristianShaw980/lab10-LC-CS
# Partner 1: Leon Calef
# Partner 2: Christian Shaw

import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        a = 1
        b = 2
        self.assertEqual(add(a,b), (a+b))

    def test_subtract(self): # 3 assertions
        a = 1
        b = 2
        self.assertEqual(subtract(a,b), (a-b))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        a = 1
        b = 2
        self.assertEqual(mul(a,b), (a*b))

    def test_divide(self): # 3 assertions
        a = 1
        b = 2
        self.assertEqual(div(a,b), (b/a))

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        a = 2
        b = 4
        self.assertEqual(logarithm(a,b), (math.log(b,a)))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self):  # 3 assertions
        a = 1
        b = 2
        self.assertEqual(hypotenuse(a,b), (math.hypot(b,a)))

    def test_sqrt(self):  # 3 assertions
        a = 256
        self.assertEqual(square_root(a), (math.sqrt(a)))

# Do not touch this
if __name__ == "__main__":
    unittest.main()
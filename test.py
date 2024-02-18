from fractions import Fraction

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main() 


"""
F.
======================================================================
FAIL: test_list_fraction (test.TestSum.test_list_fraction)
Test that it can sum a list of fractions
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\kelle\Onedrive\Desktop\SDEV-220\programs\project\test.py", line 23, in test_list_fraction     
    self.assertEqual(result, 1)
AssertionError: Fraction(9, 10) != 1

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
----------------------------------------------------------------------

This test result shows that 'Fraction(9, 10) != 1', meaning that the
fraction test failed because 9/10 is not equal to the asserted 1. 
"""
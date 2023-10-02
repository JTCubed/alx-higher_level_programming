# tests/6-max_integer_test.py
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-5, -1, -9]), -1)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)


    def test_mix(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_all_same(self):
        self.assertEqual(max_integer([9, 9, 9]), 9)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 2.8, 3.5]), 3.5)

if __name__ == "__main__":
    unittest.main()

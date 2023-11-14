import unittest
from contextlib import redirect_stdout
import sys
import io
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_attribute(self):
        r = Rectangle(5, 10, 1, 2, 42)

        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10, 1, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10, 1, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid", 1, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(5, -10, 1, 2)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "invalid", 2)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1, 2)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 1, "invalid")

        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(4, 3, 2, 1, 99)
        expected_output = "\n  ####\n  ####\n  ####\n"

        with io.StringIO() as mock_stdout, redirect_stdout(mock_stdout):
            r.display()
            actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 1, 2, 42)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 5/10")

    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)

        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_kwargs(self):
        r = Rectangle(5, 10, 1, 2, 42)
        r.update(id=9, width=15, height=25, x=3, y=2)

        self.assertEqual(r.id, 9)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 6, 7, 8)
        dictionary = r.to_dictionary()
        expected_dict = {'id': 8, 'width': 4, 'height': 5, 'x': 6, 'y': 7}
        self.assertDictEqual(dictionary, expected_dict)

if __name__ == '__main__':
    unittest.main()

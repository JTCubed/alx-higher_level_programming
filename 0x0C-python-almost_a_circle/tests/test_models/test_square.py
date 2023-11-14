import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

        s = Square(3, 2, 1, 7)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 7)

    def test_str(self):
        s = Square(4, 2, 3, 8)
        self.assertEqual(str(s), "[Square] (8) 2/3 - 4")

    def test_update_args(self):
        s = Square(2, 1, 1, 1)
        s.update(5, 10, 10, 10)
        self.assertEqual(str(s), "[Square] (5) 10/10 - 10")

    def test_update_kwargs(self):
        s = Square(3, 2, 1, 7)
        s.update(id=9, size=5, x=3, y=2)
        self.assertEqual(str(s), "[Square] (9) 3/2 - 5")

    def test_to_dictionary(self):
        s = Square(4, 2, 3, 8)
        dictionary = s.to_dictionary()
        expected_dict = {'id': 8, 'size': 4, 'x': 2, 'y': 3}
        self.assertDictEqual(dictionary, expected_dict)

if __name__ == '__main__':
    unittest.main()

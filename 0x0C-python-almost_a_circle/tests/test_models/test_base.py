import unittest

from models.base import Base

class test_Base(unittest.TestCase):

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        base_json = Base.to_json_string(None)
        self.assertEqual(base_json, '[]')

        base_json = Base.to_json_string([])
        self.assertEqual(base_json, '[]')

        base_json = Base.to_json_string([{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Doe'}])
        expected_json = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Doe"}]'
        self.assertEqual(base_json, expected_json)

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)

        Base.save_to_file([b1, b2])

        with open('Base.json', 'r') as file:
            content = file.read()
            expected_content = '[{"id": 1}, {"id": 2}]'
            self.assertEqual(content, expected_content)

    def test_from_json_string(self):
        base_list = Base.from_json_string(None)
        self.assertEqual(base_list, [])

        base_list = Base.from_json_string('[]')
        self.assertEqual(base_list, [])

        base_list = Base.from_json_string('[{"id": 1}, {"id": 2}]')
        expected_list = [{'id': 1}, {'id': 2}]
        self.assertEqual(base_list, expected_list)



if __name__ == '__main__':
    unittest.main()

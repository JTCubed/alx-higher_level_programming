#!/usr/bin/python3

"""
Class Base
"""


import json


class Base:
    """
    The superclass initiated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json formatted string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_str = cls.to_json_string([obj.to_dictionary() if hasattr(obj, 'to_dictionary') else obj.__dict__
                                           for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """from json to disctionary representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    def update(self, **kwargs):
        """Update the attributes of the instance."""
        for key, value in kwargs.items():
            setattr(self, key, value)

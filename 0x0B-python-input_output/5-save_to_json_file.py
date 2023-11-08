#!/usr/bin/python3

import json

"""writes an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        g = json.dumps(my_obj)
        write_data = f.write(g)

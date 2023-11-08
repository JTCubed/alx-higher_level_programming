#!/usr/bin/python3

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""creates an Object from a “JSON file”:"""


def add_to_list_and_save(args, filename):
    """creates an Object from a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            my_list = load_from_json_file(filename)

    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    with open(filename, 'w', encoding='utf-8') as file:
        save_to_json_file(my_list, filename)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    filename = 'add_item.json'
    add_to_list_and_save(arguments, filename)

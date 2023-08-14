#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    b = len(my_list) - 1
    if my_list is None:
        return
    for i in range(a):
        print("{:d}".format(my_list[b]))
        b -= 1

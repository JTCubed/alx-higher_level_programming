#!/usr/bin/python3
def max_integer(my_list=[]):
    a = my_list[0]
    if my_list is None:
        return (None)
    for i in my_list:
        if i >= a:
            a = i
    return (a)

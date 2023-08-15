#!/usr/bin/python3
def max_integer(my_list=[]):
    a = my_list[0]
    if my_list is None:
        return (None)
    if my_list == []:
        return (a)
    for i in my_list:
        if i >= a:
            a = i
    return (a)

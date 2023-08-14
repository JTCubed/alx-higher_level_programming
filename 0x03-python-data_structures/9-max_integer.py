#!/usr/bin/python3
def max_integer(my_list=[]):
    count = 0
    a = my_list[0]
    if len(my_list == 0):
        return (None)
    for i in my_list:
        if my_list[count] >= a:
            a = mylist[count]
        count += 1

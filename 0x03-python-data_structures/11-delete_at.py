#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list1 = my_list
    if my_list is None:
        my_list1 = []
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list1)
    else:
        return (my_list1[:idx] + my_list1[idx+1:])

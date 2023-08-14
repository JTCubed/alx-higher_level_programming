#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_s = []
    for i in my_list:
        if i % 2 == 0:
            list_s.append(True)
        else:
            list_s.append(False)
    return(list_s)

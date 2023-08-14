#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    count = 0
    for i in my_list:
        if my_list[count] % 2 == 0:
            return (True)
        else:
            return (False)
        count += 1

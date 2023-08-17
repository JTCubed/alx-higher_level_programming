#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    n = sum([a * b for a, b in my_list])
    d = sum([b for _, b in my_list])
    return (n / d if d else 0)

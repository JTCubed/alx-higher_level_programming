#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = ()
    if len(tuple_a) < 1:

        if len(tuple_b) < 2:
            a = 0, 0
        else:
            a = 0, tuple_b[1]
    else:
        if len(tuple_b) < 2:
            a = tuple_a[0] , 0
        else:
            a = tuple_a[0], tuple_b[1]
    return (a)

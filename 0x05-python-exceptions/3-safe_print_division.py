#!/usr/bin/python3

def safe_print_division(a, b):
    o = None
    try:
        o = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(o))
    return (o)

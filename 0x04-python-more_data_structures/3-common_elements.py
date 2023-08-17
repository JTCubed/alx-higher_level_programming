#!/usr/bin/python3
def common_elements(set_1, set_2):
    return [[x for j in set_2 if x in set_2 and x in set_1] for i in set_1]

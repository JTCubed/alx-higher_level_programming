#!/usr/bin/python3
"""Find peak in a list"""

def find_peak(list_of_integers):
    """Find peak in a list"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[
               mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return None

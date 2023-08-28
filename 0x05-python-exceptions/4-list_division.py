#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list3 = []

    for i in range(list_length):
        count = 0
        try:
            count = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        my_list3.append(count)
    return (my_list3)

#!/usr/bin/python3
def no_c(my_string):
    count = 0
    a = ""
    for i in my_string:
        if my_string[count] != "c" and my_string[count] != "C":
            a = a + my_string[count]
        count += 1
    return (a)

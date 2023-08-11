#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = (number * -1) % 10
        print(f"{number}", end = "")
    else:
        number = number % 10
        print(f"{number}", end = "")

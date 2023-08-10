#!/usr/bin/python3
for i in range(9):
    for j in range(9):
        print("{}{}, ".format(i, j))
        if i == 9 and j == 9:
            print()

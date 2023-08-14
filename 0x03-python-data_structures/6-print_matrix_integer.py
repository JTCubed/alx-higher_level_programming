#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    count = 0
    for i in matrix:
        for j in i:
            if j != len(i) - 1:
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j))
            print(len(row))
            count += 1

#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j):
            if ((j*10 + i) - (i * 10 + j) != -9):
                if ((j*10 + i) - (i * 10 + j) != -18):
                    if ((j*10 + i) - (i * 10 + j) != -27):
                        if ((j*10 + i) - (i * 10 + j) != -36):
                            if ((j*10 + i) - (i * 10 + j) != -45):
                                if ((j*10 + i) - (i * 10 + j) != -54):
                                    if ((j*10 + i) - (i * 10 + j) != -63):
                                        if ((j*10 + i) - (i * 10 + j) != -72):
                                            if (j != 0):
                                                if (i == 8 and j == 9):
                                                    print("{}{}".format(i, j))
                                                else:
                                                    print("{}{},".format(i, j),
                                                          end=" ")

#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
print()
mysquare = Square(89)
print(mysquare.size)
print(mysquare.area())
print()
mysquare.size = 33
print(mysquare.size)
print(mysquare.area())
print()

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

#!/usr/bin/python3
def uppercase(str):
    a = ""
    for i in str:
        if 'a' <= i <= 'z':
            a = a + chr(ord(i) - 32)
        else:
            a = a + i
    print("{}".format(a))
        
    

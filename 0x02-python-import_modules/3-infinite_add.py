#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 1
    res = 0

    for i in sys.argv[1:]:
        res = res + int(sys.argv[count])
        count += 1

    print(f"{res}")

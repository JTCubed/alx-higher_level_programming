#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 0
    count2 = 1

    for i in sys.argv:
        count += 1

    count -= 1

    if (count == 0):
        print(f"{count} arguments.")

    elif (count == 1):
        print(f"{count} argument:")
    else:
        print(f"{count} arguments:")
        if (count !=0):
            for j in sys.argv[1:]:
                print(f"{count2}: {sys.argv[count2]}")
                count2 += 1

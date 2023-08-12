#!/usr/bin/python3

if __name__ == "__main__":
    import variable_load_5

    list = dir(variable_load_5)

    for i in list:
        if i == "a":
            from variable_load_5 import a
            print(f"a = {a}")

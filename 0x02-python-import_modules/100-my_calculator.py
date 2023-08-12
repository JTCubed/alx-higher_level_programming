#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    a = 0
    b = 0

    if (len(sys.argv) != 4):
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if (sys.argv[2] == "+"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        c = add(a, b)
        print(f"{a} + {b} = {c}")

    elif (sys.argv[2] == "-"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        c = sub(a, b)
        print(f"{a} - {b} = {c}")

    elif (sys.argv[2] == "*"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        c = mul(a, b)
        print(f"{a} * {b} = {c}")

    elif (sys.argv[2] == "/"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        c = div(a, b)
        print(f"{a} / {b} = {c}")

    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

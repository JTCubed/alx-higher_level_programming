#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    c = add(a, b)
    d = sub(a, b)
    e = div(a, b)
    f = mul(a, b)

    print(f"{a} + {b} = {c}")
    print(f"{a} - {b} = {d}")
    print(f"{a} * {b} = {f}")
    print(f"{a} / {b} = {e}")

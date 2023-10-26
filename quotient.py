#!/usr/bin/env python3

a = 1
b = 1

for i in range(100000):
    q1 = 3**a / 2**b
    q2 = a / b
    if q1 > 0.999 and q1 < 1:
        print(f"{a} {b} {q1} {q2}")
    if q1 > 1:
        b += 1
    else:
        a += 1

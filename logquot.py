
from math import log, floor

def q(x):
    return 3**x/2**floor(log(3)/log(2)*x+1)

def e(x):
    return log(3)/log(2)*x - floor(log(3)/log(2)*x+1)

def q2(x):
    return 2**e(x)
    

print(q(1))
print(q2(1))
print(e(1))


m = -1
for i in range(100000000):
    k = e(i)
    if k > m:
        m=k
        print(f"{i:6d} {2**m}")


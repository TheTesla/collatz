
from math import log, floor

def q(x):
    return 3**x/2**floor(log(3)/log(2)*x+1)

def e(x):
    return log(3)/log(2)*x - floor(log(3)/log(2)*x+1)

def q2(x):
    return 2**e(x)
    

def calc_maxima(n: int):
    m = -1
    r = []
    for i in range(n):
        k = e(i)
        if k > m:
            m=k
            r.append((i,2**m))
    return r

print(calc_maxima(10))

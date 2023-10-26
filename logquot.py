from numba import jit


from math import log, floor

def q(x):
    return 3**x/2**floor(log(3)/log(2)*x+1)

@jit
def e(x):
    ex = log(3)/log(2)*x
    return ex - floor(ex + 1)

def q2(x):
    return 2**e(x)
    
@jit
def calc_maxima(n: int):
    m = -1
    r = []
    for i in range(n):
        k = e(i)
        if k > m:
            m=k
            r.append((i,2**m))
    return r

l = calc_maxima(10**11)

for i, m in l:
    print(f"{i:10} {m}")

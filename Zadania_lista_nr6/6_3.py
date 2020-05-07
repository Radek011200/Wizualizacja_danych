import numpy as np

def tab(n):
    a=np.array([[ y for y in range(x*n+1,x*n+n+1)] for x in range(0,n)] )
    return a

print(tab(10))
import numpy as np

def diag(n):
    a=np.diag([x for x in range(n,0,-1)])
    return a

print(diag(10))
import numpy as np 

def fib():
    a=1
    b=1
    n=0
    fiby=[]
    fibx=[]
    for x in range(5):
        for y in range(5):
            fiby.append(n)
            n=b
            b+=a
            a=n
            
            
            
        fibx.append(fiby)
        fiby=[]
    return np.array(fibx)
        


print(fib())

        
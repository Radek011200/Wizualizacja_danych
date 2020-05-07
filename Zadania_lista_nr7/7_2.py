import numpy as np

a = np.array( [20,30,40,50,40,7,60,70,2,] ).reshape(3,3)
b = np.array( [31,43,56,33,12,312,345,2,7,16,11,12,13,14,15,16] ).reshape(4,4)
print(a)
print(b)
print(a.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))
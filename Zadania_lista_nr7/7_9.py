import numpy as np
# generujemy macierz 1x6
b = np.arange(9).reshape(3,3)
print(b)
print
for a in b.flat:
    print(a,end=" ")
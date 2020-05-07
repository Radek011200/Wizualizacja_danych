import numpy as np
# generujemy macierz 3x2
b = np.arange(9).reshape(3,3)
print(b)
for a in range(0,b.shape[0]):
   for c in range(0,b.shape[1]):
      print(b[a,c], end=" ") 
   print(" ")
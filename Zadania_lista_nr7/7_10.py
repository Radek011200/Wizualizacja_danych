import numpy as np
b=np.arange(81).reshape(9,9)
print(b)
#przeksztalcenie
c=b.reshape(3,27)
print(c)
#splaszczenie
print(c.ravel())
#transpozycja
print(c.T)
#sa tylko takie przypadki gdyz musi zostac taka sama ilosc elementow, a w tym konkretnym przypadku jest 81 elementow
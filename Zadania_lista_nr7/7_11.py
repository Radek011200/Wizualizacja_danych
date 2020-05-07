import numpy as np

b = np.arange(12)
print(b)
c=b.reshape((3,4))
d=b.reshape((4,3))
e=b.reshape((2,6))
print(c)
print(d)
print(e)
print(c.ravel())
print(d.ravel())
print(e.ravel())
# tak sa identyczne
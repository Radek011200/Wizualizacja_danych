import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,30.1,0.1)
y= np.sin(x)
z=np.cos(x)
plt.plot(x,y, label='f(x)=sin(x)')
plt.plot(x,z, label='f(x)=cos(x)')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()
plt.title('Wykres funkcji sin(x) i cos(X) dla x ϵ [1, 30]')
plt.show()
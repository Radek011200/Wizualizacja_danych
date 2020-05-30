import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,30.1,0.1)
y2= np.sin(x)+2
z=np.sin(-x)
plt.plot(x,z, label='f(x)=sin(x+2)')
plt.plot(x,y2, label='f(x)=sin(-x)')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()
plt.title('Wykres funkcji sin(x)+2 i sin(-X) dla x ϵ [1, 30]')
plt.show()
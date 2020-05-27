import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


kolor=['green','brown','red','yellow','pink','maroon','orange','white','black','purple','gold']
kolorr=[kolor[x] for y in range(5) for x in range(0+y,6+y,1)]


fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 121 , projection = '3d' )

_x = np.arange( 6 )
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top= x+y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True,color=kolorr, lightsource=None )
ax1.set_title('Wykres po zmianach')

plt.show()
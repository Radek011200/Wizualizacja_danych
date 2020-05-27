import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):

    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
ax1 = fig.add_subplot(122, projection = '3d' )
n = 20

for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
t = np.linspace( 0 , 2 * np.pi, 5 )
z = t
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax1.plot(x, y, z, label = 'punkty', marker='x')
ax1.legend()

plt.show()
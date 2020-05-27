# Projekcja 3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

np.random.seed( 19680801 )


def randrange(n, vmin, vmax):

    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(projection = '3d' )

n = 20

for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 0 , 100 )
    ys = randrange(n, 0 , 100 )
    zs = 0
    ax.scatter(xs, ys, zs, c =c, marker ='o')

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

xs = [10,50,50,75,75,90,90]
ys = [5,5,20,20,70,70,80]
zs = 0
ax.plot(xs, ys, zs,  label = 'punkty', c='green')
ax.legend()
ax.set_zlim(0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )

plt.show()

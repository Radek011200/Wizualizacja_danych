import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


np.random.seed( 19680801 )


def randrange(n, vmin, vmax):

    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100
col=['green','blue','purple','maroon','yellow','brown','pink' ]
markers=['.',',','o','v','^','<','>','1','2','3','4','8']


for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 ), ( 'b' , '^' , - 30 , - 5 )]:
    xs = randrange(n,  23, 32 )
    ys = randrange(n, 0 , 100 )
    for x in range(1,6,1):
        zs = randrange(n, 1000, 500)   
        ax.scatter(xs, ys, zs, c =col[int(np.random.randint(0,len(col)))], marker =markers[int(np.random.randint(0,len(markers)))])

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kostka(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for x in range(n)]

IleRzutow=kostka(50)
print(IleRzutow)
plt.hist(IleRzutow, bins=7, facecolor='g', alpha=1, density=True)

plt.xlabel('Wartości')
plt.ylabel('ilosc rzutow')
plt.title('Histogram')

plt.grid(True)
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



ts = pd.Series([32134, 43242, 32432, 98754, 54332, 43345, 53123, 123453, 65789, 82354], index=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])




print(ts)
ts.plot()
plt.show()

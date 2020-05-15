import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
df=pd.read_excel(imiona,"Arkusz1")
p=df.groupby(['Rok']).agg({'Liczba':['sum']})
p.plot(xticks=p.index.values)
plt.legend()
plt.show()

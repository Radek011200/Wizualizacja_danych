import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
df=pd.read_excel(imiona,"Arkusz1")

p=df.groupby(['Plec']).agg({"Liczba":["sum"]})
p2=df.groupby(['Rok']).agg({"Liczba":["sum"]})
mezczyzna=df[df["Plec"]=='M'].groupby(['Rok']).sum()
kobieta=df[df["Plec"]=='K'].groupby(['Rok']).sum()
plt.subplot(1,3,1)
plt.bar(['Kobiety','Mezczyzni'],[p.values[0][0],p.values[1][0]],color=['brown','purple'])

plt.ylabel('ilosc')
plt.xlabel('Płeć')
plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[mezczyzna.values[y][0] for y in range(len(mezczyzna.values))],color="brown", label="Mezczyzna")
plt.plot(df.Rok.unique(),[kobieta.values[y][0] for y in range(len(kobieta.values))],color="yellow", label="Kobieta")

plt.ylabel('ilość')
plt.xlabel('rok')
plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[p2.values[y][0] for y in range(len(p2.values))],color="maroon")
plt.show()

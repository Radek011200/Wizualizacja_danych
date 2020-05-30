import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
df=pd.read_excel(imiona,"Arkusz1")
mezczyzni=df[df["Plec"]=='M'].groupby(['Rok']).sum()
kobiety=df[df["Plec"]=='K'].groupby(['Rok']).sum()
width=0.3
plt.bar(df.Rok.unique(),[mezczyzni.values[y][0] for y in range(len(mezczyzni.values))], width, color="blue",label="chlopcy")
plt.bar(df.Rok.unique(),[kobiety.values[y][0] for y in range(len(kobiety.values))], width, color="red",label="dziewczeta", bottom= [mezczyzni.values[y][0] for y in range(len(mezczyzni.values))])


plt.show()

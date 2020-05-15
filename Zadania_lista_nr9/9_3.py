import pandas as pd
import matplotlib.pyplot as plt
imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
jd=pd.read_excel(imiona,"Arkusz1")


pd=jd.agg({"Rok":['max']})
p=jd[(jd["Rok"]<= pd.values[0][0])&(jd["Rok"]> pd.values[0][0]-5)]


grupa = p.groupby(['Plec','Rok']).agg({'Liczba':['sum']})


wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('podzial')
plt.show()
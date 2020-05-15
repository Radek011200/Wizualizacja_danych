import pandas as pd
import matplotlib.pyplot as plt

imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
jd=pd.read_excel(imiona,"Arkusz1")


df = pd.DataFrame(jd, columns=['Liczba',  'Plec'])
print(df)

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chlopcow i dziewczynek')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

jd=pd.read_csv(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\zamowienia.csv", delimiter=';')
p=jd.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
wykres = p.plot.bar()
wykres.legend()
plt.title('Ilosc zamowien')
plt.show()


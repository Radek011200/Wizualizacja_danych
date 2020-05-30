import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



jd=pd.read_csv(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\zamowienia.csv", delimiter=';')
p=jd.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
sprzedawcy=p.index.values
zamowienia=[p.values[y][0] for y in range(len(p.values))]
Explode=[0 for i in range(len(p.index.values))]
Explode[5]=0.1

def prepare_label(pct, zam):
    absolute = int(np.ceil(pct / 100. * np.sum(zam)))
    return "{:.1f}% \n({}/{})".format(pct, absolute, sum(zamowienia))

wedges, texts, autotexts = plt.pie(zamowienia, explode=Explode, shadow=True, labels=sprzedawcy,
                                   autopct=lambda pct: prepare_label(pct, zamowienia), textprops=dict(color="black"))
plt.setp(autotexts, size=8, weight="bold", rotation=-45)
plt.legend(title='Sprzedawcy')
plt.show()
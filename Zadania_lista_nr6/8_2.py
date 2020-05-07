import pandas as pd
import matplotlib.pyplot as plt


data = {
'ilosc ur': [364534,  654897,  456798, 354567],
'Plec': ['chlopiec', 'dziewczyna', 'chlopiec', 'dziewczyna']}

df = pd.DataFrame(data, columns=['ilosc ur',  'Plec'])
print(df)

grupa = df.groupby(['Plec']).agg({'ilosc ur':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chlopcow i dziewczynek')
plt.show()
import pandas as pd
import numpy as np
import xlrd
import openpyxl
imiona= pd.ExcelFile(r"C:\Users\bezie\Documents\Python\__PROJEKTY\__test_virtual\imiona.xlsx")
df=pd.read_excel(imiona,"Arkusz1")

def a(df):
    print(df[df['Liczba']>1000])
def b(df):
    print(df[df['Imie']=="RADOSŁAW"])
def c(df):
    
    tabela = pd.pivot_table(df,values=['Liczba'],index=['Rok'],aggfunc=np.sum,margins=True)
    print(tabela)
def d(df):
    tabela=df[(df['Rok']>1999)&(df['Rok']<2006)]
    print(tabela.agg({'Liczba':['sum']}))
def e(df):
    tabela = pd.pivot_table(df,values=['Liczba'],index=['Plec'],aggfunc=np.sum,margins=True)
    print(tabela)
def f(df):
    tabela = df.sort_values("Liczba").groupby(['Rok', "Plec"])
    for a, b in enumerate(tabela, 1):
        print(f"{b[0]}")
        print(f"{b[1].iloc[[0],[1]].values[0][0]}",
              f"{b[1].iloc[[0],[2]].values[0][0]}")
def g(df):
    ch=df[df['Plec']=='M'].max()
    dz=df[df['Plec']=='K'].max()
    print(ch)
    print(dz)


    
#print(a(df))
#print(b(df))
#print(c(df))
#print(d(df))
#print(e(df))
#print(f(df))
#print(g(df))

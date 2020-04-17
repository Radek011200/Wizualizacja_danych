class NaZakupy():
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena_jed=0

    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa_produktu=nazwa
        self.ilosc=ilosc
        self.jednostka_miary=jednostka
        self.cena_jed=cena

    def wyswietl_produkt(self):
        print("Nazwa: ",self.nazwa_produktu)
        print("Ilosc: ",self.ilosc)
        print("Jednostka: ",self.jednostka_miary)
        print("Cena jednostkowa: ",self.cena_jed)
        
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed)


zakupy=NaZakupy("ziemniaki",10,"kg",2)
zakupy.ile_kosztuje()
zakupy.ile_produktu()
zakupy.wyswietl_produkt()
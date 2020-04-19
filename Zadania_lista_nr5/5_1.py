class Material():
    rodzaj="bawelna"
    dlugosc=0
    szerokosc=0

    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    
    def wyswietl_nazwe(self):
        print(self.rodzaj,self.dlugosc,self.szerokosc, sep="\n")
class Ubranie(Material):
    rozmiar="XL"
    kolor="zielony"
    dla_kogo="Mateusz"

    def wyswietl_dane(self):
        print(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, sep="\n")

class Sweter(Ubranie):
    rodzaj_swetra="golf"

    def wyswietl_dane(self):
        print(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_swetra, sep="\n")

bawelna=Material("naturalny",30,40)
bawelna.wyswietl_nazwe()
bluza=Ubranie("naturalny",40,50)
bluza.rozmiar="L"
bluza.kolor="biała"
bluza.dla_kogo="Tomek"
bluza.wyswietl_dane()
golf=Sweter("naturalny",30,50)
golf.rozmiar="XXL"
golf.kolor="czerwony"
golf.dla_kogo="Bartek"
golf.rodzaj_swetra="golf"
golf.wyswietl_dane()



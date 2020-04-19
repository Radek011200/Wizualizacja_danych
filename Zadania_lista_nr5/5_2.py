class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self,x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    
    def __add__(self,y):
        x=self.x+y.x
        return Kwadrat(x)
    
kw=Kwadrat(5)
print(kw)
kw1=Kwadrat(7)
print(kw1)

class Robaczek():
    x=0
    y=0
    krok=0

    def __init__(self, x, y, krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self, ile_krokow):
        self.y+=ile_krokow*self.krok
    
    def idz_w_dol(self, ile_krokow):
        self.y-=ile_krokow*self.krok
    
    def idz_w_lewo(self, ile_krokow):
        self.x-=ile_krokow*self.krok
    
    def idz_w_prawo(self, ile_krokow):
        self.x+=ile_krokow*self.krok
    
    def pokaz_gdzie_jestes(self):
        print("X: ",self.x,", Y: ",self.y)

    def __del__(self):
        del self.x
        del self.y
        del self.krok


robak=Robaczek(1,2,1)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(10)
robak.idz_w_gore(8)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(20)
robak.idz_w_dol(4)
robak.pokaz_gdzie_jestes()






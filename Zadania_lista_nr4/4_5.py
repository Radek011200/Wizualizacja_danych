class ciagarytm():
    a1=1
    r=2
    n=3

    def wyswietl_dane(self):
        print("pierwszy wyraz ciagu: ",self.a1)
        print("roznica: ",self.r)
        print("ilosc liczb: ",self.n)
    
    def pobierz_elementy(self, a1, r):
        self.a1=a1
        self.r=r

    def pobierz_parametry(self, a1, r, n):
        self.a1=a1
        self.r=r
        self.n=n 

    
    def policz_sume(self):
        return self.a1+(self.a1+(self.n-1)*self.r)/2*self.n 
        
    
   ## nie rozumiem metody policz elementy

asd=ciagarytm()
asd.wyswietl_dane()
asd.pobierz_elementy(3,5)
asd.wyswietl_dane()
print(asd.pobierz_parametry(3,5,7))
asd.wyswietl_dane()
print(asd.policz_sume())



        
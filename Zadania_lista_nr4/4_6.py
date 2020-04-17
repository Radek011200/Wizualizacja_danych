class Slowa():
    slowo1="slowo"
    slowy2="slowo2"


    def __init__(self,x,y):
        self.slowo1=x
        self.slowo2=y

    def sprawdz_czy_palindrom(self):
        print(self.slowo1, end=" ")
        if self.slowo1!=self.slowo1[::-1]:
            print("nie jest to palindrom")
        else:
            print("jest to palindrom")
        
        print(self.slowo2)
        if self.slowo2!=self.slowo2[::-1]:
            print("nie jest to palindrom")
        else:
            print("jest to palindrom")

    def sprawdz_czy_metagramy(self):
        x=0
        if len(self.slowo1)==len(self.slowo2):
            for i in range (len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    x+=1
            if x==1:
                print("nie sa to metagramy")
            else:
                print("sa to metagramy")


    def sprawdz_czy_anagramy(self):
        x=0
        if len(self.slowo1)==len(self.slowo2):
            for i in range (len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    litera = self.slowo2[i]
                    for i in range(len(self.slowo2)):
                        if litera==self.slowo2[i]:
                            x+=1
            if x==self.slowo1:
                print("sa to anagramy")
            else:
                print("nie sa to anagramy")

    def wyswietl_wyrazy(self):
        print(self.slowo1, end=" ")
        print(self.slowo2)   


wyrazy=Slowa("radar","zakaz")
wyrazy.wyswietl_wyrazy()
wyrazy.sprawdz_czy_palindrom()
wyrazy.sprawdz_czy_anagramy()
wyrazy.sprawdz_czy_metagramy()
wyrazy=Slowa("mata","tata")
wyrazy.wyswietl_wyrazy()
wyrazy.sprawdz_czy_palindrom()
wyrazy.sprawdz_czy_anagramy()
wyrazy.sprawdz_czy_metagramy()

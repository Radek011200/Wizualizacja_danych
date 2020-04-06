print("Zad 1")
print("a)")

A = [1/x for x in range(10) if x>0]
print(A)


print("b)")

B = [2**x for x in range(11)]
print(B)

print("c)")
C = [x for x in range(2**10) if x%4==0]
print(C)

print("Zad 2")


lista=[[i for i in range(1+4*j,5+4*j)] for j in range(4)]  
print(lista)
przekatna=[lista[x][x]for x in range(4)]
print(przekatna)


print("Zad 3")


produkty={"Chleb": "sztuka","Jabłka": "Kg","woda": "litr"}
print(produkty)
sztuki={x:"sztuka" for x in produkty}
print(sztuki)


print("Zad 4")


def mon(a):

    if a>0:
        print("funkcja jest rosnaca")
    elif a==0:
        print("funkcja jest stala")
    else:
        print("funkcja jest malejaca")

mon(5)


print("Zad 5")



def CzyRownoleg(a1,a2):
    if a1==a2:
        print("proste sa rownolegle")
    elif a1*a2==-1:
        print("proste sa prostopadle")
    else:
        print("proste nie sa rownolegle ani prostopadle")


CzyRownoleg(float(-0.1),float (10))



print("Zad 6")



import math
def Dlugprom(x,a,y,b):
    promien=(x-a)**2+(y-b)**2
    promien=math.sqrt(promien)
    print("Dlugosc promienia wynosi :",promien)
Dlugprom(4,2,4,2)



print("Zad 7")



def pitagoras(a,b):
    c=a**2+b**2
    c=math.sqrt(c)
    print("Dlugosc przeciwprostokatnej wynosi :",c)
    
pitagoras(3,4)



print("Zad 8")




def ciag(a,r,n):
    Suma=(2*a+(n-1)*r)/2*n 
    print("suma wynosi :",Suma)
ciag(1,1,10)




print("Zad 9")



def ciag2(*ciag):
    if(ciag)==0:
        return 0.0
    else:
        suma = 1.0 
        for i in ciag:
            suma = suma*i
        return suma
print(ciag2(1,2,3,4,5,6,7,8,9,10))




print("Zad 10")




def zakupy(**klucz):
    suma=0
    for i in klucz:
        suma+=klucz[i]
    print("Suma produktow :",suma)

zakupy(jablka=10,ser=4,chleb=1,bulka=5)


print("Zad 11 ")


from liczby_zespolone import *
x=complex(4,8)
y=complex(3,2)
rzecz_i_urojon.rzeczywista(x)
rzecz_i_urojon.urojona(x)
print(dod_i_min.dodawanie(x,y))
print(dod_i_min.odejmowanie(x,y))




print("Zad 12")



from ciagi import *

print(arytmetyczny.an(1,10,10))
print(arytmetyczny.suma(1,20,10))
print(geometryczny.an(1,2,10))
print(geometryczny.suma(1,5,5))






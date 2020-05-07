import numpy as np 

def wykreslanka():
    wyraz=['Mateusz','aasafas','tstfdka','eggeery','ufwsugh','sdsdssh','zdasddz']
    a=np.array([[x for x in wyraz[i]] for i in range(7)])

    return a

print(wykreslanka())


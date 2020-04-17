plik=open("4_1.txt","w+")
[plik.write(str(x)+" ") for x in range(1,1000) if x%4==0]

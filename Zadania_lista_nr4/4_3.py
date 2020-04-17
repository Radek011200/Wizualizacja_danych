
with open("4_1.txt", "r+") as plik:
    plik.write("to są liczby podzielne przez 4")
    for linia in plik:
        print(linia, end="")
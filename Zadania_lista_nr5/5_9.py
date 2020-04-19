def parzyste(wyraz):
    for index in range(0,len(wyraz),2):
        yield wyraz[index]

prz=parzyste("Zadanie")
print(next(prz))
print(next(prz))
print(next(prz))
print(next(prz))
print(next(prz))
print(next(prz))
print(next(prz))


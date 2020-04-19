def miesiace(liczba):
    miesiace=["styczeń","luty","marzec","kwiecień","maj","czerwiec","lipec","sierpień","wrzesień","październik","listopad","grudzień"]
    for index in range(0,len(miesiace),1):
        yield  miesiace[index]

mies=miesiace(12)
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))



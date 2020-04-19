class Samogloski:
    samogloski={"a","e","i","o","u","y"}

    def __init__(self, wyraz):
        if isinstance(wyraz,str):
            self.wyraz=wyraz
        else:
            self.wyraz=str(wyraz)
        self.x=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.x +=1
        if self.x >= len(self.wyraz):
            raise StopIteration
        if self.wyraz[self.x] in Samogloski.samogloski:
            return self.wyraz[self.x]

wyr=Samogloski("Zadanie")
w=iter(wyr)
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
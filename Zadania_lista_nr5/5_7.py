class Parzyste:
    def __init__(self, wyraz):
        self.wyraz=wyraz
        self.index=-2

    def __iter__(self):
        return self
    
    def __next__(self):
        
        self.index +=2
        if self.index >= len(self.wyraz):
                raise StopIteration
        return self.wyraz[self.index]




Slowo=Parzyste("Zadanie")
slo=iter(Slowo)
print(next(slo))
print(next(slo)) 
print(next(slo)) 
print(next(slo)) 
print(next(slo)) 
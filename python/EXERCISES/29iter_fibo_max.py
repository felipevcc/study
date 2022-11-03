# FIBONACCI + max (ITERATORS)

from time import sleep

class FiboIter():
    
    def __init__(self, max=None):
        self.max = max 

    def __iter__(self):
        self.n1 = 0 
        self.n2 = 1
        self.counter = 0
        return self 

    def __next__(self):
        if not self.max or self.n2 < self.max:
            if self.counter == 0:
                self.counter += 1 
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2 
            else:
                # Pasar un lugar a la derecha en la sucesión:
                self.aux = self.n1 + self.n2 
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux # swap/swapping
                self.counter += 1
                return self.aux

        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = FiboIter(8)
    # recorrer el __next__ de la class:
    for element in fibonacci:
        print(element)
        sleep(1) # pausar 1 seg antes de seguir a la sgte vuelta 

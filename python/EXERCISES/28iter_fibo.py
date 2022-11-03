# FIBONACCI (ITERATORS)

import time

class FiboIter():
    
    def __iter__(self):
        self.n1 = 0 
        self.n2 = 1
        self.counter = 0
        return self 

    def __next__(self):
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

if __name__ == "__main__":
    fibonacci = FiboIter()
    # recorrer el __next__ de la class:
    for element in fibonacci:
        print(element)
        time.sleep(1) # pausar 1 seg antes de seguir a la sgte vuelta 

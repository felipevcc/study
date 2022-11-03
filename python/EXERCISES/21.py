#2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
from itertools import permutations
lista = ['a','e','i','o','u']
combinaciones = permutations(lista)
for i in combinaciones:
    print(''.join(i))
#EJERCICIO 30
try:
    n = nmax = 0
    while n >= 0:
        n = int(input("Dame un número positivo: "))
        nmax = max(nmax, n)
finally:
    print(f"No se admiten negativos como {n}. El número más elevado fue el: {nmax}")
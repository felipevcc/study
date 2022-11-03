def rectangulo(ancho, alto):
    caracter = '*'
    resultado = ''
    for j in range(alto+1):
        for i in range(ancho+1):
            resultado = resultado + caracter
        resultado = resultado + '\n'
    print(resultado)
rectangulo(6,4)
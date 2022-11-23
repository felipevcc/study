"""
Andres Felipe Villamizar C.
Ficha: 2547401


ACTIVIDAD: Algoritmo/Codigo para el calculo de areas y volumenes


EXPLICACION PARA LA EJECUCION:

Para ejecutar el archivo desde la terminal usar el siguiente comando:
python calc.py

Para ir escogiendo figuras a lo largo de la ejecución simplemente
digite el numero de la figura correspondiente y presione enter

Para ir dando los valores a las longitudes se las figuras
solamente escribe el valor y presione enter

"""

from time import sleep

def fig_plana():
    figura = int(input("\nFigura:\n[1] Triangulo\n[2] Cuadrado\nDigite el numero [1/2]: "))
    if (figura != 1 and figura != 2):
        print("\nSolo estan permitidos los numeros 1 y 2, intentalo de nuevo...")
        sleep(1.5)
        return fig_plana()

    long_lados = float(input("\nLongitud de un lado en cm: "))
    if (long_lados < 0):
        print("\nError! No es posible calcular con longitud negativa")
        exit()

    if (figura == 1):
        cant_lados = 3
        altura = float(input("Longitud de la altura en cm: "))
        area = long_lados * altura / 2
    else:
        cant_lados = 4
        area = long_lados * long_lados

    perimetro = long_lados * cant_lados
    
    print("\nRESULTADOS")
    print(f"\nPerimetro: {perimetro} cm")
    print(f"Area: {area} cm^2")


def fig_solida():
    figura = int(input("\nFigura:\n[1] Cubo\n[2] Prisma cuadrangular\nDigite el numero [1/2]: "))
    if (figura != 1 and figura != 2):
        print("\nSolo estan permitidos los numeros 1 y 2, intentalo de nuevo...")
        sleep(1.5)
        return fig_solida()
    
    if (figura == 1):
        lado = float(input("\nLongitud de una arista en cm: "))
        volumen = lado ** 3
    else:
        base = float(input("\nLongitud de una arista de la base: "))
        altura = float(input("Longitud de la altura: "))
        volumen = (base ** 2) * altura

    print("\nRESULTADO")
    print(f"\nVolumen: {volumen} cm^3")


def main(): 
    print("\n=== CALCULOS DE FIGURAS ===\n")
   
    categoria_figura = int(input("Tipo de figura:\n[1] Plana\n[2] Solida\nDigite el numero [1/2]: "))
    if (categoria_figura == 1):
        fig_plana()
    elif (categoria_figura == 2):
        fig_solida()
    else:
        print("\nSolo estan permitidos los numeros 1 y 2, intentalo de nuevo...")
        sleep(1.5)
        return main() 

if __name__ == '__main__':
    main()

preguntasClave = int(input("Digite su contraseña"))
if preguntasClave == 1234:
    print("Bienvenido al cajero de los mejores")
    i = 0
    saldo = []
    while i <= 10:
        suma = sum(saldo)
        
        def cajero():
            if suma == 1:
                print(suma)
            menu = ["1)Ingresar saldo","2)Retirar dinero"]
            for i in menu:
                print(i)
            preguntaMenu = int(input("Que deseas realizar"))
            if preguntaMenu == 1:
                print(suma)
                IngresarDinero = int(input("Cuanto dinero deseas ingresar"))
                saldo.append(IngresarDinero)
                x = input('Que')
                if x == 0:
                    print('')
                elif x == 1:
                    return cajero()

                

            elif preguntaMenu == 2:
                disminuirDinero = int(input("Cuanto dinero deseas retirar"))
                resultado = suma - disminuirDinero
                print(resultado)
                y = input('Que')
                if y == 0:
                    print('')
                elif y == 1:
                    return cajero()
        cajero()
        
        
        i +=1
else:
   pass
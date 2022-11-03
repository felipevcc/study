preguntasClave = int(input("Digite su contraseña"))
if preguntasClave == 1234:
    print("Bienvenido al cajero de los mejores")
    i = 0
    saldo = []
    while i <= 10:
        print(sum(saldo))
        def cajero():
            menu = ["1)Ingresar saldo","2)Retirar dinero"]
            print(menu)
            #for i in menu:
                #print(i)
            preguntaMenu = int(input("Que deseas realizar"))
            if preguntaMenu == 1:
                IngresarDinero = int(input("Cuanto dinero deseas ingresar"))
                saldo.append(IngresarDinero)
        cajero()
        i +=1
else:
   pass
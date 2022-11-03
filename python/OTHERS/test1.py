"""Se debe permitir:
1##registrar el número de documento de identidad del votante =============
2##Ofrecerle el listado de candidatos de una corporación.==========
3##Registrar el voto===========
4##Ofrecerle el listado de candidatos de la otra corporación.================
5#Registrar el voto=============
6##Cerrarle el proceso de votación al elector
7#No permitir que ese Numero de cédula vuelva a votar======================
8#Generar los resultados de las elecciones al finalizar el proceso de votación: gnadores por cada corporación y 
cantidad de votos en blanco para cada una, cantidad total de votantes y en cada corporación, total y 
9#porcentaje de hombres y de mujeres votantes."""

#Arreglo Para registrar los ID
mayorVotos= 0 
mayorVotos2 = 0
Numerocedula = []
#Arreglo para registrar la cantidad de votantes 
CantidadVotantesHombres=[]
CantidadVotantesMujeres=[]
#Matriz para corporacion 1
Corporacion1 = [[1, 2, 3],
                [4, 5, 6]]
#Matriz para corporacion 2
Corporacion2 = [[1, 2, 3],
                [4, 5, 6]]
votos  = [0,0,0,0,0,0]
votos2  = [0,0,0,0,0,0]
#Que va a pasar con esto? Pues en el GUI se le va a explicar al votante que si desea votar por X candidato marque
#Asi: Ejemplo: El votante renan lodi, sera mostrado en la corporacion 2, y su posicion es 0,0 en la matriz
#Si el votante desea votar por Renan Lodi, debera marcar 0,0 en el GUI

#Poner un break cuando no hayan mas votantes (Boton que cierre la votacion)
def repfuncion():
#Funcion para llamarla en tkinter y tener los datos guardados en arreglos. 
    def datosDelVotante(): 
        NumeroDoc = int(input("Ingrese el numero de la CC: "))
        while NumeroDoc in Numerocedula:
                print("No puede votar, debido a que ya tiene registrado un voto. ")
                NumeroDoc = int(input("Ingrese un numero de CC distinto: "))
        else: 
                Numerocedula.append(NumeroDoc)
    datosDelVotante()
                    
                    
    #Funcion para sumarle +1 voto dependiendo el sexo. 
    def votantesHombresOmujer(): 
        sexo = input("Ingrese sexo = masculino o femenino (En minuscula)")
        if sexo=="masculino":
            CantidadVotantesHombres.append(+1)
        if sexo=="femenino":
            CantidadVotantesMujeres.append(+1)
    votantesHombresOmujer()
    #


    
     #JuanitoPerez,Margarita, JoseHenao, MargotPerez, Valentina, Blanco. 
    #mayorVotos= max(votos) #Funcion para sacar el maximo de una lista. 
    votos.index(mayorVotos)
    def corporacioNumero1(): 
        corporacioNumero1 = int(input("Marque Un numero: "))
        if corporacioNumero1== Corporacion1[0][0]:  
            votos[0] +=1
        elif corporacioNumero1==Corporacion1[0][1]:
            votos[1] +=1
        elif corporacioNumero1==Corporacion1[0][2]:
            votos[2] +=1
        elif corporacioNumero1==Corporacion1[1][0]:
            votos[3] +=1
        elif corporacioNumero1==Corporacion1[1][1]:
            votos[4] +=1
        elif corporacioNumero1==Corporacion1[1][2]: 
            votos[5] +=1
        

    corporacioNumero1()

     #Esto es para la corporacion 2
    #mayorVotos2= max(votos2) #Funcion para sacar el maximo de una lista. 
    votos2.index(mayorVotos2)
    def corporacioNumero2(): 
        
        corporacioNumero2 = int(input("Marque Un numero: "))
        if corporacioNumero2== Corporacion2[0][0]:  
            votos2[0] +=1
        elif corporacioNumero2==Corporacion2[0][1]:
            votos2[1] +=1
        elif corporacioNumero2==Corporacion2[0][2]:
            votos2[2] +=1
        elif corporacioNumero2==Corporacion2[1][0]:
            votos2[3] +=1
        elif corporacioNumero2==Corporacion2[1][1]:
            votos2[4] +=1
        elif corporacioNumero2==Corporacion2[1][2]: 
            votos2[5] +=1
        
    corporacioNumero2()      
    
    def preguntilla():
        pregunta = input("Escriba si o no (En minuscula) si desea cerrar el proceso. ")
        if pregunta == "no": 
            return repfuncion()  
        else: 
            print(f"La votacion ha terminado, {votos[5]}, cantidad voto blanco para corporacion1")
            print(f"El ganador de la corporacion 1 fue {max(votos)}")
            print(f"La votacion ha terminado, {votos2[5]}, cantidad voto blanco para corporacion2")
            print(f"El ganador de la corporacion 2 fue: {max(votos2)}")
    
    preguntilla()
    
repfuncion()
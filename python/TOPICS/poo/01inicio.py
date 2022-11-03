#PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

#Paradigma de desarrollo, al igual que la programacion funcional o imperativa

#de la clase derivan los objetos
#siempre primera letra mayuscula
class Casa:
    #x = 10
    #pass para dejar vacia la clase
    #init es una funcion para asignar valores
    #self siempre va de primero porque hace referencia asi mismo
    def __init__(self, nombre, años):
        self.name = nombre
        self.age = años #para activar los parametros
    def funcion(self):
        print("Hola mundo desde python " + self.name)
    
#objetos e instancias:
objeto = Casa("Luis", 17)
print(objeto.name) 
print(objeto.age)#para acceder al valor por medio del objeto
objeto.funcion()

objeto2 = Casa("Mateo", 27)
print(objeto2.name, objeto2.age) #tambien se puede asi
objeto2.funcion()



#Ejemplos mas sencillos:

class Auto:
    marca = " "
    modelo = 2004
    placa = " "

taxi = Auto()
print(taxi.modelo)



class Persona:
    doctor = "Felipe"

print(Persona.doctor) 

#______________________________

class Nombre:
    pass

victor = Nombre()
maria = Nombre()

#objeto.atributo = valor
victor.edad = 30
victor.genero = "Masculino"
victor.pais = "Colombia"

maria.edad = 25
maria.genero = "Femenino"
maria.pais = "Mexico"

print(victor.edad)
print(maria.edad)

#_________________________________

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)
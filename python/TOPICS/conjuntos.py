#CONJUNTOS (set)

#Los conjuntos son una coleccion desordenada
#Se escriben con llaves {} 

#no permite valores duplicados (dos buses no acepta, solo uno)

mi_conjunto = {"carro", "moto", "bus"}
print(len(mi_conjunto))
print(mi_conjunto)

#los conjuntos tampoco se pueden llamar por medio de indices o claves
#una vez creados son inmutables, incambiables

mi_conjunto_entero = {1,8,4,6}
print(mi_conjunto_entero)

mi_conjunto_mixto = {"python", 17, True, 1.50}
print(mi_conjunto_mixto)

#set() contructor para realizar un conjunto
vehiculos = set(("banano", "mora", "piña"))
print(type(vehiculos))

frutas = {"rojo", "amarillo"}
print("negro" in frutas) #devuelve una respuesta en booleano

add = {"rojo", "amarillo"}
frutas.add("pink")
print(frutas)
#siempre que se va a agregar un metodo es con ()

#cargar un conjunto a otro
update1 = {"marron", "morado"}
update2 = {"amarillo", "naranja"}
update1.update(update2)
print(update1)
print(type(update1))

#remover
marcas = {"bmw", "mercedez"}
marcas.remove("bmw")
print(marcas)

#eliminar
ftas = {"naranja", "mandarina"}
ftas.discard("naranja")
print(ftas)

#metodo pop()
motos = {"honda", "bmw"}
x = motos.pop()
print(x)

patinetas = {"roja", "amarilla", "azul"}
del patinetas
#print(patinetas)

#union
pc1 = {"dell", "levono", "samsung"}
pc2 = {"mac", "hp"}
z = pc1.union(pc2)
print(z)

#___________________________________
#metodo intersection_update()
indate1 = {"mora", "piña", "banano"}
indate2 = {"mora", "fresa", "banano"}

indate1.intersection_update(indate2)
print(indate1)#en el mismo conjunto

#metodo intersection()
indate3 = {"mora", "piña", "banano"}
indate4 = {"mora", "fresa", "banano"}

w= indate3.intersection(indate4)
print(w)#en diferente conjunto (x)
#________________________________________

#metodo symmetric_difference_update()
indate5 = {"mora", "piña", "banano"}
indate6 = {"mora", "fresa", "banano"}

indate5.symmetric_difference_update(indate6)
print(indate5)#mismo conjunto

#metodo symetric_difference()
indate7 = {"mora", "piña", "banano"}
indate8 = {"mora", "fresa", "banano"}
y= indate7.symmetric_difference(indate8)
print(y)#diferente conjunto



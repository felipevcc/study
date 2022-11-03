#Para escribir en un txt
f = open('files.txt', 'a')
f.write('\n' + 'Estamos escribiendo desde python')
f.close()

#append = 'a'
#'w' = elimina todo y solo deja lo ultimo que se escribio

#Para llamar y mostrar un txt
f = open('files.txt')
print(f.read())
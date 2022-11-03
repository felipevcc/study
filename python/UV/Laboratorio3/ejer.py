print('\n==================CENSO VIRTUAL==================\n')

n = input('Nombre: ')
ape = input('Apellido: ')
documento = input('Tipo de documento de identidad: ')
n_doc = input('Número de documento de identidad: ')
nacmto = input('Fecha de nacimiento: ')
dep = input('Departamento de nacimiento: ')
ciudad_natal = input('Ciudad de nacimiento: ')
direccion = input('Dirección de residencia: ')
familiares = int(input('Cantidad de familiares a registrar: '))

nombre = [None]*familiares
apellido = [None]*familiares
ti = [None]*familiares
num_ti = [None]*familiares
nacimiento = [None]*familiares
parentesco = [None]*familiares

for i in range(familiares):
    nombre[i] = input('\nNombre: ')
    apellido[i] = input('Apellido: ')
    ti[i] = input('Tipo de documento de identidad: ')
    num_ti[i] = input('Número de documento de identidad: ')
    nacimiento[i] = input('Fecha de nacimiento: ')
    parentesco[i] = input('Parentesco: ')


print('\n' + ('='*20) + 'JEFE DEL HOGAR'+('='*20)+'\n')

print(f'NOMBRE: {n}\nAPELLIDO: {ape}\nTIPO DE DOCUMENTO: {documento}\nDOCUMENTO: {n_doc}\nFECHA NACIMIENTO: {nacmto}\nDEPARTAMENTO\nCIUDAD: {ciudad_natal}\nDIRECCIÓN: {direccion}\nCANT. FAMILIARES: {familiares}')

print('\n' + ('='*20) + 'FAMILIARES'+('='*20)+'\n')

for i in range(familiares):
    print('\nNOMBRE:', nombre[i])
    print('APELLIDO:', apellido[i])
    print('TIPO DE DOCUMENTO:', ti[i])
    print('DOCUMENTO:', num_ti[i])
    print('FECHA DE NACIMIENTO:', nacimiento[i])
    print('PARENTESCO:', parentesco[i])

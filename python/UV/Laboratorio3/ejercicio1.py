"""
Integrantes : 
Nombre : Johan Andres Lopez Garcia
Codigo : 2179543

Nombre : Andres Felipe Villamizar C.
Codigo : 2180436

FUNDAMENTOS DE PROGRAMACION IMPERATIVA - GRUPO 81
Profesora : Diana Patricia Lozano

Laboratorio No. 3 Estructuras de repeticion

Problema 1: 
    Se va a llevar a cabo una primera fase del censo nacional de manera virtual. 
    Para ello, los ciudadanos deben registrar sus datos personales y algunos datos 
    de las personas que conforman su hogar en una plataforma diseñada con este fin. 
    La persona que ingresa a la plataforma será el(la) jefe de hogar y debe 
    proporcionar los siguientes nueve datos:

        • Nombre 
        • Apellido 
        • Tipo de documento de identidad 
        • Número de documento de identidad 
        • Fecha de nacimiento 
        • Departamento de nacimiento 
        • Ciudad de nacimiento 
        • Dirección de residencia 
        • Cantidad de familiares a registrar 

    Posteriormente, para cada miembro del hogar se deben registrar los siguientes seis datos: 

        • Nombre 
        • Apellido 
        • Tipo de documento de identidad 
        • Número de documento de identidad 
        • Fecha de nacimiento 
        • Parentesco

    Al finalizar el registro, se debe mostrar una confirmación con todos los datos proporcionados.
"""

def run():
    print('\n' + ('='*20) + 'CENSO VIRTUAL'+('='*20)+'\n')

    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    documento = input('Tipo de documento: ')
    num_documento = input('Número de documento: ')
    nacimiento = input('Fecha de nacimiento: ')
    departamento = input('Departamento de nacimiento: ')
    ciudad_natal = input('Ciudad de nacimiento: ')
    direccion = input('Dirección de residencia: ')
    familiares = int(input('Cantidad de familiares a registrar: '))

    flia = ('\n' + '=====FAMILIAR {num}=====' + '\n' + 
                '\nNombre: {nombre_familiar}\n' + 
                'Apellido: {apellido_familiar} \n' +
                'Tipo de documento: {documento_familiar}\n' + 
                'Número de documento: {num_documento_familiar}\n' + 
                'Fecha de nacimiento: {nacimiento_familiar}\n' + 
                'Parentesco: {parentesco_familiar}\n')

    datos_familiares = ''

    contador = 0
    for i in range(1,familiares+1):
        print(f'\nREGISTRE AL FAMILIAR #{i}\n')
        nombre_familiar = input('Nombre: ')
        apellido_familiar = input('Apellido: ')
        documento_familiar = input('Tipo de documento: ')
        num_documento_familiar = input('Número de documento: ')
        nacimiento_familiar = input('Fecha de nacimiento: ')
        parentesco_familiar = input('Parentesco: ')

        datos_familiares += (flia.format(num = i,
                                nombre_familiar = nombre_familiar, 
                                apellido_familiar = apellido_familiar, 
                                documento_familiar = documento_familiar, 
                                num_documento_familiar = num_documento_familiar, 
                                nacimiento_familiar = nacimiento_familiar,
                                parentesco_familiar = parentesco_familiar))
    
    print('\n' + ('='*20) + 'JEFE DEL HOGAR'+('='*20)+'\n')
    print(f'NOMBRE: {nombre}\nAPELLIDO: {apellido}\nTIPO DE DOCUMENTO: {documento}\nDOCUMENTO: {num_documento}\nFECHA NACIMIENTO: {nacimiento}\nDEPARTAMENTO\nDEPARTAMENTO: {departamento}\nCIUDAD: {ciudad_natal}\nDIRECCIÓN: {direccion}\nCANT. FAMILIARES: {familiares}')

    print('\n' + ('='*20) + 'FAMILIARES'+('='*20)+'\n')
    print(datos_familiares)

if __name__ == '__main__':
    run()
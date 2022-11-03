print('\n---VENTAS---')
producto = input('\nNombre del producto: ')
valor = int(input('Valor: $'))
ventas = int(input('Cantidad de unidades vendidas: '))
datos = (f'\nNombre: {producto}\nValor: ${valor}\nVendidos: {ventas}')
iva = 0.19
x = datos
y = ventas
m = valor

if valor >= 0 and ventas >= 0:
    while valor >= 0 and ventas >= 0: 
        producto = input('\nNombre del producto: ')
        valor = int(input('Valor: $'))
        ventas = int(input('Cantidad de unidades vendidas: ')) 
        datos = (f'\nNombre: {producto}\nValor: ${valor}\nVendidos {ventas}')
        if valor >= 0 and ventas >= 0:
            x = f'{x}\n{datos}'
            y = y + ventas
            m = m + valor
    iva_global = (m * iva) * y
    print(f'\n---INVENTARIO---')
    print(f'\nPRODUCTOS:\n{x}')
    print('\nVENTAS AL DIA:', y)
    print(f'\nVALOR GLOBAL COBRADO POR CONCEPTO DE IVA: ${iva_global}')
else:
    print('\nNo hay datos digitados')
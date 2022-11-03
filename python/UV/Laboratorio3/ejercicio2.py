"""
Integrantes : 
Nombre : Johan Andres Lopez Garcia
Codigo : 2179543

Nombre : Andres Felipe Villamizar C.
Codigo : 2180436

FUNDAMENTOS DE PROGRAMACION IMPERATIVA - GRUPO 81
Profesora : Diana Patricia Lozano

Laboratorio No. 3 Estructuras de repeticion

Problema 2 : 
Pago de empleados en Univalle
Este programa permite a la Division de Recursos Humanos de la Universidad, calcular el neto
a pagar para cada uno de sus empleados.

# DATOS DE ENTRADA :

    - cantidad_empleados -> entero : Este parametro indica la cantidad de veces que se iterara
                                    en el programa, teniendo en cuenta que por cada empleado
                                    se realizara una iteracion.

    *   Por cada iteracion se solicitara :
        - numero_documento  -> String : En esta variable se almacenara el numero de documento
                                        del empleado
        - nombre_empleado   -> String : En esta variable se almacenara el nombre del empleado,
                                        en este caso, preferiblemente el nombre completo.
        - salario_empleado  -> double : En esta variable se almacenara el salario del empleado.


# DATOS DE SALIDA : 
En este programa se muestra la siguiente informacion :
    *   PAGOS 
        - Salario
        - Bonificacion de servicios
        - subsidio de transporte
    *   DESCUENTOS
        - Salud
        - Pension
        - Retefuente
    *   TOTAL PAGOS - DESCUENTOS
    Esto por cada empleado ingresado.
"""

def run():

    # Constantes : Porcentajes de Pagos
    PORCENTAJE_SUBSIDIO_TRANSPORTE    = 0.2    # 20% Salario Base
    PORCENTAJE_BONIFICACION_SERVICIOS = 0.1    # 10% Salario Base

    # Constantes : Porcentajes descuentos
    PORCENTAJE_SALUD      = 0.04   # 4% Salario Base
    PORCENTAJE_PENSION    = 0.04   # 4% Salario Base
    PORCENTAJE_RETEFUENTE = 0.05   # 5% Salario Base

    # Constantes : Mensajes en consola 
    MENSAJE_ADVERTENCIA =  ('\n' + ('=' * 10) + ' ADVERTENCIA ' + ('=' * 10) + '\n' + 
                            'Solo puede ingresar numeros positivos, los cuales corresponden a la cantidad de empleados a procesar.' + '\n' + 
                            ('=' * 33) + '\n')
    MENSAJE_ERROR       =  ('\n' + ('=' * 10) + ' ERROR ' + ('=' * 10) + '\n' + 
                            'Has sobrepasado la cantidad de errores permitidos, ejecuta el programa nuevamente.' + '\n' + 
                            ('=' * 33) + '\n')
    
    # Plantillas
    datos_empleado      = ('\n' + ('=' * 20) + ' DATOS DEL EMPLEADO  {numerador} ' + ('=' * 20) + '\n' + 
                          'Nombre : {nombre_empleado}\n' + 
                          'Documento : {numero_documento} \n')
    
    pagos_empleado      = ('\n' + ('=' * 20) + ' PAGOS ' + ('=' * 20) + '\n' + 
                         'Salario : {salario_base} \n' + 
                         'Bonificacion de Servicios : {bonificacion_servicios} \n' + 
                         'Subsidio de Transporte : {subsidio_transporte} \n' )
    
    descuentos_empleado = ('\n' + ('=' * 20) + ' DESCUENTOS ' + ('=' * 20) + '\n' + 
                         'Salud : {salud} \n' + 
                         'Pension : {pension} \n' + 
                         'Retefuente : {retefuente} \n' )

    totales             = ('\n' + ('=' * 20) + ' TOTALES ' + ('=' * 20) + '\n' + 
                         'Total Pagos : {total_pagos} \n' + 
                         'Total Descuentos : {total_descuentos} \n' + 
                         'Neto Pagar : {neto_pagar} \n' )


    # Variable acumuladora :
    resultado = ''

    # Paso 1 : Solicitud de la cantidad de empleados a procesar  =================
    error_tipo                  = True
    cantidad_errores_permitidos = 3
    while error_tipo and cantidad_errores_permitidos > 0:
        try:
            cantidad_empleados_procesar = int(input('Ingrese la cantidad de empleados a procesar : '))
            if cantidad_empleados_procesar > 0:
                error_tipo = False
            else:
                raise Exception
        except Exception:            
            print(MENSAJE_ADVERTENCIA)
            cantidad_errores_permitidos -= 1
    

    # Paso 2 : Solicitud de informacion de cada empleado a procesar =============
    if cantidad_errores_permitidos > 0:
        for empleado in range(0, cantidad_empleados_procesar, 1):
            print('\n' + ('=' * 20) + f' REGISTRO DEL EMPLEADO  {empleado+1} ' + ('=' * 20) + '\n')
            numero_documento = input('Digite el numero de documento de identidad : ')
            nombre_empleado  = input('Digite el nombre completo : ')
            salario_base     = float(input('Digite el salario base del empleado : '))

            # Paso 3 : Calculo de pagos y descuentos =============================
            resultado_bonificacion_servicios = salario_base * PORCENTAJE_BONIFICACION_SERVICIOS
            resultado_subsidio_transporte    = salario_base * PORCENTAJE_SUBSIDIO_TRANSPORTE

            resultado_descuento_salud        = salario_base * PORCENTAJE_SALUD
            resultado_descuento_pension      = salario_base * PORCENTAJE_PENSION
            resultado_descuento_retefuente   = salario_base * PORCENTAJE_RETEFUENTE

            resultado_total_pagos            = salario_base + resultado_bonificacion_servicios + resultado_subsidio_transporte
            resultado_total_descuentos       = resultado_descuento_salud + resultado_descuento_pension + resultado_descuento_retefuente 
            resultado_neto_pagar             = resultado_total_pagos - resultado_total_descuentos

            resultado += (datos_empleado.format(numerador = (empleado + 1), nombre_empleado = nombre_empleado, numero_documento = numero_documento) + 
                         pagos_empleado.format(salario_base = salario_base, bonificacion_servicios = resultado_bonificacion_servicios, subsidio_transporte = resultado_subsidio_transporte) +
                         descuentos_empleado.format(salud = resultado_descuento_salud, pension = resultado_descuento_pension, retefuente = resultado_descuento_retefuente) + 
                         totales.format(total_pagos = resultado_total_pagos, total_descuentos = resultado_total_descuentos, neto_pagar = resultado_neto_pagar))
            

        print(resultado)
    else :
        print(MENSAJE_ERROR)


if __name__ == '__main__':
    run()
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:49:59 2020

@author: SYSTEM
"""

import numpy as np
from .libreria_loteria import (lee_datos,conseguir_secuencias_iguales,secuencias_con_iguales_sin_orden,
                              conjuntos_N_iguales_sin_orden,determina_los_numeros_distintos,
                              veces_que_ocurrio_un_numero,obtiene_frecuencias,obtiene_matriz_datos_dia,
                              almacenar_datos_excel,obtiene_mayor_y_menor,obtiene_frecuencias_de_frecuencias)
from .libreria_grafica import (grafica_en_ventana_general)
from .combinaciones import (obtiene_las_N_mayores_frecuencias,obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas,
                           obtiene_las_N_menores_frecuencias)

import csv

def calcula_frecuencias_dia(dia):
    #######################################
    ## Leer los datos del Lotto Texas    ##   
    #######################################

    control_filas=0
    nro_filas=10
    N=54
    (matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)=lee_datos(control_filas,nro_filas)
    
    ######################################################################################
    ## los números que aparecen en la matriz de datos                                   ##
    ######################################################################################
    numeros_distintos=determina_los_numeros_distintos(matriz_de_datos)
    print("Cantidad de números ditintos ordenados: ",len(numeros_distintos))
    
    ######################################################################################
    ## Los números y su frecuencia en la matriz de datos                                ##
    ######################################################################################
    (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_de_datos)
    print("Los números: ", los_numeros)
    print("las frecuencias: ",las_frecuencias)

    
    #########################################################
    # Los números que más han salido los sábados/miércoles  #
    #########################################################
    print(cadena_dia_semana)
    if (dia=="Sábado"):
        matriz_sabados=obtiene_matriz_datos_dia(dia,cadena_dia_semana,matriz_de_datos)
    if (dia=="Miércoles"):
        matriz_miercoles=obtiene_matriz_datos_dia(dia,cadena_dia_semana,matriz_de_datos)
    
    ##############################################################################################
    # Obtener los números que corresponden a las N frecuencias más altas, los sábados/miércoles  #
    ##############################################################################################

    if (dia=="Sábado"):
        matriz_dia=matriz_sabados   
    if (dia=="Miércoles"):
        matriz_dia=matriz_miercoles
         
    numeros_distintos_dia=determina_los_numeros_distintos(matriz_dia)
    print("Cantidad de números ditintos ordenados: ",len(numeros_distintos_dia))
    (los_numeros_dia,frecuencias_dia)=obtiene_frecuencias(numeros_distintos_dia,matriz_dia)
    print("Los números: ", los_numeros_dia)
    print("las frecuencias",frecuencias_dia)
    mayores_frecuencias_dia=obtiene_las_N_mayores_frecuencias(N,frecuencias_dia)
    print("Las mayores frecuencias sábados/miércoles: ",mayores_frecuencias_dia)
    print("las frecuencias originales originales",frecuencias_dia)
    (los_numeros_dia,frecuencias_dia)=obtiene_frecuencias(numeros_distintos_dia,matriz_dia)
    
    print("Los números sábado/miércoles: ", los_numeros_dia)
    print("las frecuencias sábado/miércoles",frecuencias_dia)
    listado_frecuencias,listado_numeros=obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas(los_numeros_dia,mayores_frecuencias_dia,frecuencias_dia)
    print("listado_numeros: ", listado_numeros)
    print("listado_frecuencias: ",listado_frecuencias)
    

    #####################################################################################
    # Almacenar las frecuencias de mayor a menor y sus números, los miércoles/sábados   #
    #####################################################################################
    if (dia=="Sábado"):
        nombre_archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/resultados_solo_sabados.csv"
    if (dia=="Miércoles"):
        nombre_archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/resultados_solo_miercoles.csv"   
    with open(nombre_archivo, 'w',newline='',encoding="utf-8") as csvfile:
            campos = ['Número', 'Frecuencia']
            #writer = csv.DictWriter(csvfile, fieldnames=campos,delimiter=';')
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            for j in range(0,len(listado_numeros)):
                writer.writerow({'Número': str(listado_numeros[j]), 'Frecuencia': str(listado_frecuencias[j])})
    return



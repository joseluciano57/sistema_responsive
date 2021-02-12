# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:49:59 2020

@author: SYSTEM
"""
from datetime import (date,datetime,timedelta)
import numpy as np
from .libreria_loteria import (lee_datos,conseguir_secuencias_iguales,secuencias_con_iguales_sin_orden,
                              conjuntos_N_iguales_sin_orden,determina_los_numeros_distintos,
                              veces_que_ocurrio_un_numero,obtiene_frecuencias,obtiene_matriz_datos_dia,
                              almacenar_datos_excel,obtiene_mayor_y_menor,obtiene_frecuencias_de_frecuencias,
                              obtiene_matriz_datos_dia_mes_semana,obtiene_matriz_datos_dia_mes)
from .libreria_grafica import (grafica_en_ventana_general)
from .combinaciones import (obtiene_las_N_mayores_frecuencias,obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas,
                           obtiene_las_N_menores_frecuencias)

import csv

def frecuencias_dia_mes():  
    #######################################
    ## Leer los datos del Lotto Texas    ##   
    #######################################
    control_filas=0
    nro_filas=10
    
    (matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)=lee_datos(control_filas,nro_filas)
    print("Fechas: ",cadena_fecha_jugada)
    print("Días: ",cadena_dia_semana)
    print("semanas: ",semana_del_mes)
    
    """
    fecha_final=date.today()
    fecha_string = datetime.strftime(fecha_final, '%Y-%m-%d')
    mes=fecha_string[5:7]
    print("mes: ",mes)
    """
    
    dias=["Sábado","Miércoles"]
    mes=["01","02","03","04","05","06","07","08","09","10","11","12"]
    nombre_mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    
    for dia in dias:
        for i in range(0,len(mes)):
            matriz_datos_combinadas=[]
            print(dia,i)
            matriz_datos_combinadas=obtiene_matriz_datos_dia_mes(dia,cadena_dia_semana,mes[i],cadena_fecha_jugada,matriz_de_datos)
            print(matriz_datos_combinadas)
    
            #### Obtener los números de mayor frecuencia por día y mes ####    
            numeros_distintos=determina_los_numeros_distintos(matriz_datos_combinadas)
            print("Cantidad de números ditintos ordenados: ",len(numeros_distintos))
            (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_datos_combinadas)
            print("Los números: ", los_numeros)
            print("las frecuencias: ",las_frecuencias)
        
            ## Obtener los números que corresponden a las N frecuencias más altas               ##
            N=len(las_frecuencias)
            mayores_frecuencias=obtiene_las_N_mayores_frecuencias(N,las_frecuencias)
            print("Las mayores frecuencias distintas: ",mayores_frecuencias)
            print("las frecuencias originales originales: ",las_frecuencias)
            (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_datos_combinadas)
            print("las frecuencias originales originales: ",las_frecuencias)
            frecuencia_de_frecuencias=obtiene_frecuencias_de_frecuencias(mayores_frecuencias,las_frecuencias)
            print("las frecuencias de frecuencias: ",frecuencia_de_frecuencias)
            print("Totalidad de los números: ",sum(frecuencia_de_frecuencias))
            
            listado_frecuencias,listado_numeros=obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas(los_numeros,mayores_frecuencias,las_frecuencias)
            print("Los números con ocurrencias_altas: ", listado_numeros)
            print("las frecuencias más altas: ",listado_frecuencias)
            
            nombre_archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/archivo_"+ dia + "_" + nombre_mes[i] +".csv"    
            with open(nombre_archivo, 'w',newline='',encoding="utf-8") as csvfile:
                campos = ['Número', 'Frecuencia']
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                for j in range(0,len(listado_numeros)):
                    writer.writerow({'Número': str(listado_numeros[j]), 'Frecuencia': str(listado_frecuencias[j])})
    
    
    return
      
    
    
    

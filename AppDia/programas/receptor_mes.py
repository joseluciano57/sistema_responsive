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

def calcula_frecuencias_de_los_meses(): 
    #######################################
    ## Leer los datos del Lotto Texas    ##   
    #######################################
    control_filas=0
    nro_filas=10
    
    (matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)=lee_datos(control_filas,nro_filas)
    print("fecha_jugada:",cadena_fecha_jugada)
    
    ### Crea las matrices de datos de cada mes
    datos_1=[]
    datos_2=[]
    datos_3=[]
    datos_4=[]
    datos_5=[]
    datos_6=[]
    datos_7=[]
    datos_8=[]
    datos_9=[]
    datos_10=[]
    datos_11=[]
    datos_12=[]
    for i in range(0,matriz_de_datos.shape[0]):
        fila_datos=[]
        for j in range(0,matriz_de_datos.shape[1]):
            fila_datos.append(matriz_de_datos[i,j])
       
        mes=cadena_fecha_jugada[i][5:7]
        if (mes=="01"):
            datos_1.append(fila_datos)
        if (mes=="02"):
            datos_2.append(fila_datos)    
        if (mes=="03"):
            datos_3.append(fila_datos)        
        if (mes=="04"):
            datos_4.append(fila_datos)    
        if (mes=="05"):
            datos_5.append(fila_datos)   
        if (mes=="06"):
            datos_6.append(fila_datos)
        if (mes=="07"):
            datos_7.append(fila_datos)
        if (mes=="08"):
            datos_8.append(fila_datos) 
        if (mes=="09"):
            datos_9.append(fila_datos)
        if (mes=="10"):
            datos_10.append(fila_datos)
        if (mes=="11"):
            datos_11.append(fila_datos) 
        if (mes=="12"):
            datos_12.append(fila_datos)    
    
    datos_mes_1=np.array(datos_1,int)
    datos_mes_2=np.array(datos_2,int)
    datos_mes_3=np.array(datos_3,int)
    datos_mes_4=np.array(datos_4,int)
    datos_mes_5=np.array(datos_5,int)
    datos_mes_6=np.array(datos_6,int)
    datos_mes_7=np.array(datos_7,int)
    datos_mes_8=np.array(datos_8,int)
    datos_mes_9=np.array(datos_9,int)
    datos_mes_10=np.array(datos_10,int)
    datos_mes_11=np.array(datos_11,int)
    datos_mes_12=np.array(datos_12,int)
    
    
    ### Por cada mes ####       
    for i in range(1,13):
        ######################################################################################
        ## los números que aparecen en la matriz de datos del mes                           ##
        ######################################################################################
        matriz_de_datos=[]
        filas_de_datos=[]
        
        if (i==1):
            el_mes="enero"
            for k in range(0,datos_mes_1.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_1.shape[1]):
                    columnas_de_datos.append(datos_mes_1[k,t])
                filas_de_datos.append(columnas_de_datos)        
                       
        if (i==2):
            el_mes="febrero"
            for k in range(0,datos_mes_2.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_2.shape[1]):
                    columnas_de_datos.append(datos_mes_2[k,t])
                filas_de_datos.append(columnas_de_datos)
    
        if (i==3):
            el_mes="marzo"
            for k in range(0,datos_mes_3.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_3.shape[1]):
                    columnas_de_datos.append(datos_mes_3[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==4):
            el_mes="abril"
            for k in range(0,datos_mes_4.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_4.shape[1]):
                    columnas_de_datos.append(datos_mes_4[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==5):
            el_mes="mayo"
            for k in range(0,datos_mes_5.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_5.shape[1]):
                    columnas_de_datos.append(datos_mes_5[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==6):
            el_mes="junio"
            for k in range(0,datos_mes_6.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_6.shape[1]):
                    columnas_de_datos.append(datos_mes_6[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==7):
            el_mes="julio"
            for k in range(0,datos_mes_7.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_7.shape[1]):
                    columnas_de_datos.append(datos_mes_7[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==8):
            el_mes="agosto"
            for k in range(0,datos_mes_8.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_8.shape[1]):
                    columnas_de_datos.append(datos_mes_8[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==9):
            el_mes="septiembre"
            for k in range(0,datos_mes_9.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_9.shape[1]):
                    columnas_de_datos.append(datos_mes_9[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==10):
            el_mes="octubre"
            for k in range(0,datos_mes_10.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_10.shape[1]):
                    columnas_de_datos.append(datos_mes_10[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==11):
            el_mes="noviembre"
            for k in range(0,datos_mes_11.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_11.shape[1]):
                    columnas_de_datos.append(datos_mes_11[k,t])
                filas_de_datos.append(columnas_de_datos)
        if (i==12):
            el_mes="diciembre"
            for k in range(0,datos_mes_12.shape[0]):
                columnas_de_datos=[]
                for t in range(0,datos_mes_12.shape[1]):
                    columnas_de_datos.append(datos_mes_12[k,t])
                filas_de_datos.append(columnas_de_datos)
    
        matriz_de_datos=np.array(filas_de_datos,int)
        print("Matriz_de_datos: ",matriz_de_datos)
    
        numeros_distintos=determina_los_numeros_distintos(matriz_de_datos)
        print("Cantidad de números ditintos ordenados: ",len(numeros_distintos))
        (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_de_datos)
        print("Los números: ", los_numeros)
        print("las frecuencias: ",las_frecuencias)
    
         
        ######################################################################################
        ## Obtener los números que corresponden a las N frecuencias más altas               ##
        ######################################################################################
        N=54
        
        mayores_frecuencias=obtiene_las_N_mayores_frecuencias(N,las_frecuencias)
        print("Las mayores frecuencias distintas: ",mayores_frecuencias)
        print("las frecuencias originales originales: ",las_frecuencias)
        (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_de_datos)
        print("las frecuencias originales originales: ",las_frecuencias)
        frecuencia_de_frecuencias=obtiene_frecuencias_de_frecuencias(mayores_frecuencias,las_frecuencias)
        print("las frecuencias de frecuencias: ",frecuencia_de_frecuencias)
        print("Totalidad de los números: ",sum(frecuencia_de_frecuencias))
        
        listado_frecuencias,listado_numeros=obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas(los_numeros,mayores_frecuencias,las_frecuencias)
        print("Los números con ocurrencias_altas: ", listado_numeros)
        print("las frecuencias más altas: ",listado_frecuencias)
        
        nombre_archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/archivo_"+ el_mes +".csv"    
        with open(nombre_archivo, 'w',newline='',encoding="utf-8") as csvfile:
                campos = ['Número', 'Frecuencia']
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                for j in range(0,len(listado_numeros)):
                    writer.writerow({'Número': str(listado_numeros[j]), 'Frecuencia': str(listado_frecuencias[j])})
    """    
        ##################################################################
        #    Almacenar las frecuencias de mayor a menor y sus números    #
        ##################################################################
        dataframe_resultados={'Frecuencia':listado_frecuencias,
                              'Número':listado_numeros}
        
        columnas=['Frecuencia','Número']
        nombre_archivo="todos_los_resultados.xlsx"
        almacenar_datos_excel(nombre_archivo,dataframe_resultados,columnas)
        
        
           
        """
    
    
def calcula_frecuencias_mes(mes_consultado): 
    #######################################
    ## Leer los datos del Lotto Texas    ##   
    #######################################
    control_filas=0
    nro_filas=10
    
    (matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)=lee_datos(control_filas,nro_filas)
    print("fecha_jugada:",cadena_fecha_jugada)
    
    ### Crea las matrices de datos de cada mes
    datos_1=[]
    datos_2=[]
    datos_3=[]
    datos_4=[]
    datos_5=[]
    datos_6=[]
    datos_7=[]
    datos_8=[]
    datos_9=[]
    datos_10=[]
    datos_11=[]
    datos_12=[]
    for i in range(0,matriz_de_datos.shape[0]):
        fila_datos=[]
        for j in range(0,matriz_de_datos.shape[1]):
            fila_datos.append(matriz_de_datos[i,j])
       
        mes=cadena_fecha_jugada[i][5:7]
        if (mes=="01"):
            datos_1.append(fila_datos)
        if (mes=="02"):
            datos_2.append(fila_datos)    
        if (mes=="03"):
            datos_3.append(fila_datos)        
        if (mes=="04"):
            datos_4.append(fila_datos)    
        if (mes=="05"):
            datos_5.append(fila_datos)   
        if (mes=="06"):
            datos_6.append(fila_datos)
        if (mes=="07"):
            datos_7.append(fila_datos)
        if (mes=="08"):
            datos_8.append(fila_datos) 
        if (mes=="09"):
            datos_9.append(fila_datos)
        if (mes=="10"):
            datos_10.append(fila_datos)
        if (mes=="11"):
            datos_11.append(fila_datos) 
        if (mes=="12"):
            datos_12.append(fila_datos)    
    
    datos_mes_1=np.array(datos_1,int)
    datos_mes_2=np.array(datos_2,int)
    datos_mes_3=np.array(datos_3,int)
    datos_mes_4=np.array(datos_4,int)
    datos_mes_5=np.array(datos_5,int)
    datos_mes_6=np.array(datos_6,int)
    datos_mes_7=np.array(datos_7,int)
    datos_mes_8=np.array(datos_8,int)
    datos_mes_9=np.array(datos_9,int)
    datos_mes_10=np.array(datos_10,int)
    datos_mes_11=np.array(datos_11,int)
    datos_mes_12=np.array(datos_12,int)
    
    
    ### Para el mes seleccionado####       

    ######################################################################################
    ## los números que aparecen en la matriz de datos del mes                           ##
    ######################################################################################
    matriz_de_datos=[]
    filas_de_datos=[]
    
    if (mes_consultado==1):
        el_mes="enero"
        for k in range(0,datos_mes_1.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_1.shape[1]):
                columnas_de_datos.append(datos_mes_1[k,t])
            filas_de_datos.append(columnas_de_datos)        
                   
    if (mes_consultado==2):
        el_mes="febrero"
        for k in range(0,datos_mes_2.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_2.shape[1]):
                columnas_de_datos.append(datos_mes_2[k,t])
            filas_de_datos.append(columnas_de_datos)

    if (mes_consultado==3):
        el_mes="marzo"
        for k in range(0,datos_mes_3.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_3.shape[1]):
                columnas_de_datos.append(datos_mes_3[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==4):
        el_mes="abril"
        for k in range(0,datos_mes_4.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_4.shape[1]):
                columnas_de_datos.append(datos_mes_4[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==5):
        el_mes="mayo"
        for k in range(0,datos_mes_5.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_5.shape[1]):
                columnas_de_datos.append(datos_mes_5[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==6):
        el_mes="junio"
        for k in range(0,datos_mes_6.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_6.shape[1]):
                columnas_de_datos.append(datos_mes_6[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==7):
        el_mes="julio"
        for k in range(0,datos_mes_7.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_7.shape[1]):
                columnas_de_datos.append(datos_mes_7[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==8):
        el_mes="agosto"
        for k in range(0,datos_mes_8.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_8.shape[1]):
                columnas_de_datos.append(datos_mes_8[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==9):
        el_mes="septiembre"
        for k in range(0,datos_mes_9.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_9.shape[1]):
                columnas_de_datos.append(datos_mes_9[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==10):
        el_mes="octubre"
        for k in range(0,datos_mes_10.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_10.shape[1]):
                columnas_de_datos.append(datos_mes_10[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==11):
        el_mes="noviembre"
        for k in range(0,datos_mes_11.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_11.shape[1]):
                columnas_de_datos.append(datos_mes_11[k,t])
            filas_de_datos.append(columnas_de_datos)
    if (mes_consultado==12):
        el_mes="diciembre"
        for k in range(0,datos_mes_12.shape[0]):
            columnas_de_datos=[]
            for t in range(0,datos_mes_12.shape[1]):
                columnas_de_datos.append(datos_mes_12[k,t])
            filas_de_datos.append(columnas_de_datos)

    matriz_de_datos=np.array(filas_de_datos,int)
    print("Matriz_de_datos: ",matriz_de_datos)

    numeros_distintos=determina_los_numeros_distintos(matriz_de_datos)
    print("Cantidad de números ditintos ordenados: ",len(numeros_distintos))
    (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_de_datos)
    print("Los números: ", los_numeros)
    print("las frecuencias: ",las_frecuencias)

     
    ######################################################################################
    ## Obtener los números que corresponden a las N frecuencias más altas               ##
    ######################################################################################
    N=54
    
    mayores_frecuencias=obtiene_las_N_mayores_frecuencias(N,las_frecuencias)
    print("Las mayores frecuencias distintas: ",mayores_frecuencias)
    print("las frecuencias originales originales: ",las_frecuencias)
    (los_numeros,las_frecuencias)=obtiene_frecuencias(numeros_distintos,matriz_de_datos)
    print("las frecuencias originales originales: ",las_frecuencias)
    frecuencia_de_frecuencias=obtiene_frecuencias_de_frecuencias(mayores_frecuencias,las_frecuencias)
    print("las frecuencias de frecuencias: ",frecuencia_de_frecuencias)
    print("Totalidad de los números: ",sum(frecuencia_de_frecuencias))
    
    listado_frecuencias,listado_numeros=obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas(los_numeros,mayores_frecuencias,las_frecuencias)
    print("Los números con ocurrencias_altas: ", listado_numeros)
    print("las frecuencias más altas: ",listado_frecuencias)
    
    nombre_archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/archivo_"+ el_mes +".csv"    
    with open(nombre_archivo, 'w',newline='',encoding="utf-8") as csvfile:
            campos = ['Número', 'Frecuencia']
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            for j in range(0,len(listado_numeros)):
                writer.writerow({'Número': str(listado_numeros[j]), 'Frecuencia': str(listado_frecuencias[j])})
    return
    
    
    
    
    
    
    
    

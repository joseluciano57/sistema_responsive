# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 09:41:42 2020

@author: Luciano
"""

import numpy as np
from datetime import datetime
import pandas as pd
from .combinaciones import obtiene_matriz_combinaciones

#######################################################################################
# Función que lee los datos del excel y los devuelve en forma de vectores y matrices. #
# Se puede indicar cuántas filas se requieren para la matriz.                         #
#######################################################################################
def lee_datos(control_filas,nro_filas):
    #df = pd.read_excel('C:/Users/Luciano/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/lottotexas.xlsx')
    df = pd.read_excel('C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/lottotexas.xlsx')
    
    columnas = ['TYPE', 'DATE', 'DAY_OF_WEEK','WK_NUM_YR', 'WK_NUM_MO', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6']
    
    print('TYPE    DATE   DAY_OF_WEEK   WK_NUM_YR   WK_NUM_MO   B1  B2  B3  B4  B5  B6')   
    
    tipo_loteria=df[columnas[0]]
    fecha_de_jugada=df[columnas[1]]
    dia_semana=df[columnas[2]]
    semana_del_ayo=df[columnas[3]]
    semana_del_mes=df[columnas[4]]
    b1=df[columnas[5]]
    b2=df[columnas[6]]
    b3=df[columnas[7]] 
    b4=df[columnas[8]]  
    b5=df[columnas[9]]
    b6=df[columnas[10]]
    
    print()
    
    if (control_filas==0):
        nro_filas=len(df)
                     
    cadena_fecha_jugada=[]
    cadena_dia_semana=[]
    for i in range(nro_filas):
        
        dia_string = datetime.strftime(dia_semana[i], '%Y-%m-%d')
        #print(fecha_string)
        dia=dia_string[9:10]
        #print(dia)
        dia_cadena=int(dia)
        if (dia_cadena==4):
            #print("Miércoles")
            dia_jugada="Miércoles"        
        if (dia_cadena==7): 
            #print("Sábado")
            dia_jugada="Sábado"
        
        fecha_string = datetime.strftime(fecha_de_jugada[i], '%Y-%m-%d')
        #print(fecha_string)
        cadena_fecha_jugada.append(fecha_string)
        cadena_dia_semana.append(dia_jugada)
        print("{} {} {} {} {} {} {} {} {} {} {}"
              .format(tipo_loteria[i],fecha_string,dia_jugada,semana_del_ayo[i],semana_del_mes[i],b1[i],b2[i],b3[i],b4[i],b5[i],b6[i]))
    
       
    #print("Crear un vector con los datos")
    vector_de_datos=[]
    for i in range(nro_filas):    
            vector_de_datos.append(b1[i])
            vector_de_datos.append(b2[i])
            vector_de_datos.append(b3[i])
            vector_de_datos.append(b4[i])
            vector_de_datos.append(b5[i])
            vector_de_datos.append(b6[i])
            
    #print(vector_de_datos) 
    
    print("La matriz de datos")
    #filas=len(df_seleccionados)
    filas=nro_filas
    columnas=6
    
    matriz_de_datos=np.array(vector_de_datos).reshape(filas,columnas)
    print(matriz_de_datos)
    

    return(matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)

##############################################################################################
# Función que compara un vector con cada fila de una matriz y cuenta las veces que coinciden.#
##############################################################################################
def compara_filas(vector,matriz):
    contador_fila_completa=0
    
    for i in range(0,matriz.shape[0]):
        contador_elementos_fila=0
        for j in range(0,matriz.shape[1]):
            if (vector[j]==matriz[i,j]):
                contador_elementos_fila=contador_elementos_fila + 1
        if (contador_elementos_fila == len(vector)):
            contador_fila_completa = contador_fila_completa + 1
                       
    return (contador_fila_completa)



##########################################################################################
# Función que determina el número de veces que se ha repetido una secuencia de números.  #
# Es decir, una secuencia exacta, los números apareciendo en el mismo orden.             #
##########################################################################################
def conseguir_secuencias_iguales(matriz):
    filas= 0
    vector_de_iguales=[]
    frecuencia_de_jugada=[]
    for i in range(0,matriz.shape[0]):
        vector_fila=[]
        for j in range(0,matriz.shape[1]):
            vector_fila.append(matriz[i,j])
        contador=compara_filas(vector_fila,matriz)                 
        if (contador > 1):
            print("El vector {} se repite {} veces".format(vector_fila,contador-1))
            filas=filas + 1
            vector_de_iguales.append(vector_fila)
            frecuencia_de_jugada.append(contador -1)
    
    columnas=6
    if (filas > 1):
        matriz_de_iguales=np.array(vector_de_iguales).reshape(filas,columnas)
        print(matriz_de_iguales)
    else:
        matriz_de_iguales=[]
    return (matriz_de_iguales,frecuencia_de_jugada,filas)
    

##############################################################################################
# Función que compara un vector con cada fila de una matriz y cuenta las veces que coinciden.#
# Sin importar el orden de los números.                                                      #
##############################################################################################
def compara_filas_sin_orden(vector,matriz):
    contador_fila_completa=0
    
    for i in range(0,matriz.shape[0]):
        contador_elementos_fila=0
        vector_igual=[]
        for j in range(0,matriz.shape[1]):
            for k in range(0,matriz.shape[1]):
                if (vector[j]==matriz[i,k]):
                    contador_elementos_fila=contador_elementos_fila + 1
                    vector_igual.append(matriz[i,k])
        
        contador=0
        if (contador_elementos_fila == len(vector)):
            for j in range(0,matriz.shape[1]):
                control=0
                for k in range(0,matriz.shape[1]):
                    if (vector[j]==vector_igual[k]):
                        control=1
                if (control==1):
                    contador=contador+1
                                                 
        if (contador_elementos_fila == len(vector) and contador == len(vector)  ):
            contador_fila_completa = contador_fila_completa + 1
            if (contador_fila_completa > 1):
                print("Vector igual:", vector_igual)
                       
    return (vector_igual,contador_fila_completa)
######################################################################################################
# Función que determina el número de veces que han salido los mismos números sin importar el orden.  #
######################################################################################################
def secuencias_con_iguales_sin_orden(matriz):
    filas= 0
    vector_de_iguales=[]
    frecuencia_de_jugada=[]
    for i in range(0,matriz.shape[0]):
        vector_fila=[]
        for j in range(0,matriz.shape[1]):
            vector_fila.append(matriz[i,j])
        (vector_igual,contador)=compara_filas_sin_orden(vector_fila,matriz)                 
        if (contador > 1):
            print("El vector sin orden {} se repite {} veces".format(vector_fila,contador-1))
            filas=filas + 1
            vector_de_iguales.append(vector_fila)
            frecuencia_de_jugada.append(contador -1)
            
    columnas=6
    if (filas > 1):
        matriz_de_iguales=np.array(vector_de_iguales).reshape(filas,columnas)
        print(matriz_de_iguales)
    else:
        matriz_de_iguales=[]

    return (matriz_de_iguales,frecuencia_de_jugada,filas)


##############################################################################################
# Función que cuenta las veces que un subconjunto de una jugada se ha repetido en todas las  #
# jugadas.                                                                                   #
##############################################################################################
def compara_filas_N_sin_orden(vector,matriz,N):
    
    contador_apariciones=0
    
    for i in range(0,matriz.shape[0]):
        contador_elementos_fila=0
        fila_matriz=[]
        fila_matriz_auxiliar=[]
        for j in range(0,matriz.shape[1]):
                fila_matriz.append(matriz[i,j])
                fila_matriz_auxiliar.append(matriz[i,j])
        
        #vector_igual=[]
        for j in range(0,N):
            for k in range(0,matriz.shape[1]):
                if (vector[j]==fila_matriz[k]):
                    contador_elementos_fila=contador_elementos_fila + 1
                    #vector_igual.append(fila_matriz[k])
                    fila_matriz[k]=-1
                    break
                
        if (contador_elementos_fila == N):
            contador_apariciones = contador_apariciones + 1
            #print(fila_matriz)
            print(fila_matriz_auxiliar)                   
    return contador_apariciones
###################################################################################################
# Función que determina el número de veces que ha salido un subconjunto, de tamaño N, de cada     #
# jugada en todas las jugadas, sin importar el orden.                                             #
###################################################################################################
def conjuntos_N_iguales_sin_orden(N,matriz):
    filas= 0
    vector_de_iguales=[]
    frecuencia_de_jugada=[]
    frecuencias_de_combinacion=[]
    repeticiones=0
    vector_de_conjuntos_repetidos=[]
    if (N>=1 and N <=6):         
        for i in range(0,matriz.shape[0]):
            vector_fila=[]
            for j in range(0,matriz.shape[1]):
                vector_fila.append(matriz[i,j])
            #print("Combinaciones de la fila: ",i+1)
            (matriz_combinaciones,combinaciones)=obtiene_matriz_combinaciones(vector_fila,N)
            for j in range(0,matriz_combinaciones.shape[0]):
                vector_combinacion=[]
                for k in range(0,matriz_combinaciones.shape[1]):
                    vector_combinacion.append(matriz_combinaciones[j,k])
                
                filas=filas + 1
                vector_de_iguales.append(vector_combinacion)
                
                contador=compara_filas_N_sin_orden(vector_combinacion,matriz,N)    
                
                frecuencia_de_jugada.append(contador)

                #print("Conjunto sin orden {}  Nro. de apariciones: {} ".format(combinaciones[j],contador))
        columnas=6
        matriz_combinaciones_totales=np.array(vector_de_iguales).reshape(filas,columnas)
        #print(matriz_de_iguales)
        for k in range(0,matriz_combinaciones_totales.shape[0]):
            if (frecuencia_de_jugada[k] > 1):
                frecuencias_de_combinacion.append(frecuencia_de_jugada[k])
                repeticiones=repeticiones + 1
                for j in range(0,matriz_combinaciones_totales.shape[1]):
                    vector_de_conjuntos_repetidos.append(matriz_combinaciones_totales[k,j])
        if (repeticiones > 0):
            matriz_combinaciones_finales=np.array(vector_de_conjuntos_repetidos).reshape(repeticiones,columnas)
        else:
            matriz_combinaciones_finales=[]         
    else:
        print("El tamaño del conjunto está fuera del rango")
        matriz_combinaciones_finales=[]
    return (matriz_combinaciones_finales,frecuencias_de_combinacion,repeticiones)

##############################################################################################
# Función que determina si un vector está o no en una matriz. (No importa cuantas veces).      #
##############################################################################################
def buscar_vector_en_matriz(vector,matriz):
    existe=0
    for i in range(0,matriz.shape[0]):
        fila_matriz=[]
        for j in range(0,matriz.shape[1]):
            fila_matriz.append(matriz[i,j])
        
        contador_elementos_fila=0    
        for j in range(0,matriz.shape[1]):
            for k in range(0,matriz.shape[1]):
                if (vector[j]==fila_matriz[k]):
                    contador_elementos_fila=contador_elementos_fila + 1
                    fila_matriz[k]=-1
                    break
        if (contador_elementos_fila == len(vector)):
            existe=1
            break
    return existe
###################################################################################################
# Función que obtiene sólo las combinaciones diferentes de una matriz de combinaciones.           #
###################################################################################################
def obtiene_total_combinaciones_diferentes(matriz):
    fila_inicial=[]
    matriz_diferentes=[]
    vector_basura=[]
    for k in range(0,matriz.shape[1]):
            vector_basura.append(0)
    matriz_diferentes.append(vector_basura) #Esto, para poder tener una matriz inicialmente y no un vector
        
    for k in range(0,matriz.shape[1]):
            fila_inicial.append(matriz[0,k]) 
    matriz_diferentes.append(fila_inicial)
    
    #print(matriz_diferentes)

    matriz_diferentes_finales=np.array(matriz_diferentes).reshape(2,6)       
    nro_combinaciones_diferentes= 2 #" porque tengo una fila inicial ficticia, llena de ceros
   
    for i in range(0,matriz.shape[0]):
        fila=[]
        for j in range(0,matriz.shape[1]):
                fila.append(matriz[i,j])
                
        existe=buscar_vector_en_matriz(fila,matriz_diferentes_finales) 
                    
        if (existe==0):
             matriz_diferentes.append(fila)
             nro_combinaciones_diferentes = nro_combinaciones_diferentes + 1
             matriz_diferentes_finales=np.array(matriz_diferentes).reshape(nro_combinaciones_diferentes,6) 
    
    vector_de_filas=[]
    for i in range(1,nro_combinaciones_diferentes):
        fila=[]
        for j in range(0,matriz_diferentes_finales.shape[1]):
            fila.append(matriz_diferentes_finales[i,j])
        vector_de_filas.append(fila)
        
    matriz_final=np.array(vector_de_filas).reshape(nro_combinaciones_diferentes - 1,6) 
                                   
    return (matriz_final,nro_combinaciones_diferentes - 1)
###################################################################################################
# Función que obtiene todas las combinaciones de tamaño N, de toda la matriz                      #
# de datos, sin importar el orden.                                                                #
###################################################################################################
def obtiene_total_combinaciones_tamano_N_sin_orden(N,matriz):
    filas= 0
    vector_combinacion=[]
    if (N>=1 and N <=6):         
        for vector_fila in list(matriz):
            (matriz_combinaciones,combinaciones)=obtiene_matriz_combinaciones(vector_fila,N)
            for fila_combinacion in list(matriz_combinaciones):
                vector_combinacion.append(fila_combinacion)
                filas=filas + 1
        columnas=6
        matriz_combinaciones_finales=np.array(vector_combinacion).reshape(filas,columnas)
        
    else:
        print("El tamaño del conjunto está fuera del rango")
        matriz_combinaciones_finales=[]           
    return (matriz_combinaciones_finales)



###################################################################################################
# Función que determina los números diferentes que han salido en todas las jugadas.               #
###################################################################################################
def determina_los_numeros_distintos(matriz):
    numeros=[]
    numeros.append(matriz[0,0])
    for i in range(0,matriz.shape[0]):
        for j in range(0,matriz.shape[1]):
            repetido=0
            for k in numeros:
                if (matriz[i,j]==k):
                    repetido=1
            if (repetido==0):
                numeros.append(matriz[i,j])
    vector=sorted(numeros)                
    print("Los distintos números desordenados: ",numeros) 
    print("Los distintos números ordenados: ",vector)       
    return (vector)


###########################################################################################
## Función que determina la cantidad de veces que ha ocurrido un número.                 ##
###########################################################################################
def veces_que_ocurrio_un_numero(numero,matriz):
    nro_veces=0
    for i in range(0,matriz.shape[0]):
        for j in range(0,matriz.shape[1]):
            if (numero==matriz[i,j]):
                nro_veces = nro_veces + 1              
    return nro_veces

#################################################################################################
## Función que obtiene las frecuencias (las veces que se repite en el conjunto) de cada número.##
#################################################################################################
def obtiene_frecuencias(numeros,matriz):
    frecuencias=np.zeros(len(numeros), dtype=int,order='C')
    print("Tamaño: ", len(frecuencias))
    k=0
    for numero in numeros:
        frecuencia_numero=veces_que_ocurrio_un_numero(numero,matriz)
        frecuencias[k]=frecuencia_numero
        print("Número: {}  Frecuencia: {}".format(numero,frecuencias[k]))
        k=k+1         
    return (numeros,frecuencias)

#################################################################################################
## Función que obtiene las veces que aparece cada frecuencia en el vector de frecuencias.      ##
#################################################################################################
def obtiene_frecuencias_de_frecuencias(frecuencias_distintas,frecuencias_totales):
    repeticion_frecuencia=np.zeros(len(frecuencias_distintas), dtype=int,order='C')
    k=0
    for i in frecuencias_distintas:
        nro_veces=0
        for j in frecuencias_totales:
                if (j==i):
                    nro_veces = nro_veces + 1 
        repeticion_frecuencia[k]=nro_veces
        k=k+1
               
    return (repeticion_frecuencia)

###################################################################################
# Función que obtiene una matriz con los números que salieron el sábado/miércoles.#
###################################################################################
def obtiene_matriz_datos_dia(dia,vector_dias,matriz_datos):
    matriz=[]
    nro_filas=0
    vector_de_datos=[]
    for i in range(0,len(vector_dias)):
        if (vector_dias[i]==dia):
            nro_filas=nro_filas + 1
            for k in range(0,6):
                vector_de_datos.append(matriz_datos[i,k])

    print(vector_de_datos) 
    
    print("Crear la matriz de datos")
    filas=nro_filas
    columnas=6
    
    matriz=np.array(vector_de_datos).reshape(filas,columnas)
    print(matriz)          
    
    return(matriz)

#######################################################################################
# Función que guardar datos a excel.                                                  #
#######################################################################################
def almacenar_datos_excel(nombre_archivo,datos,columnas):
    
    print(nombre_archivo)
    print(datos)
    print(columnas)
    df=pd.DataFrame(datos,columns=columnas)
    df.to_excel(nombre_archivo)
    
    return

#######################################################################################
# Función que obtiene el elemento mayor y el elemento menor de una matriz.            #                                     #
#######################################################################################
def obtiene_mayor_y_menor(matriz):
    numero_mayor=np.max(matriz)
    numero_menor=np.min(matriz)
    
    return (numero_mayor,numero_menor)

###########################################################################################
## Función que ordena las combinaciones diferentes según su frecuencia, de mayor a menor ##
###########################################################################################
def ordena_combinaciones_frecuencia_mayor_menor(frecuencias,matriz):
    mayores_frecuencias=[]
    #mayores_frecuencias_finales=[]
    vector_filas=[]
    frecuencias_auxiliares=[]

    for i in range(0,len(frecuencias)):
        frecuencias_auxiliares.append(frecuencias[i])

    for i in range(0,len(frecuencias)):
        mayor=np.max(frecuencias)
        if (mayor != -1):
            for j in range(0,len(frecuencias)):
                    if (frecuencias[j]==mayor):
                        mayores_frecuencias.append(mayor) 
                        frecuencias[j]=-1
    
    print("Nro frecuencias: ",len(mayores_frecuencias))
    print("Frecuencias originales",frecuencias_auxiliares)
    frecuencias=frecuencias_auxiliares
    print("Frecuencias originales",frecuencias)
    print("Frecuencias mayores",mayores_frecuencias)
    print("La matriz de entrada de combinaciones diferentes: ",matriz)
    
    fila=[]
    for i in range(0,len(mayores_frecuencias)):
        frecuencia_mayor=mayores_frecuencias[i]
        columnas=[]
        for j in range(0,len(frecuencias)):
            if (frecuencias[j]==frecuencia_mayor):
                for k in range(0,matriz.shape[1]):
                    vector_filas.append(matriz[j,k])
                    
                    columnas.append(matriz[j,k])
                frecuencias[j]=-1   
                    
                #mayores_frecuencias_finales.append(frecuencia_mayor)
                fila.append(columnas)
                matriz_ordenada=np.array(fila,int)
                break
            

                
                
    """            
    print("Vector: ",vector_filas)
    print("Longitud:",len(vector_filas))
    
    print("La matriz: ",matriz.shape)
    
    matriz_ordenada=np.array(vector_filas).reshape(len(frecuencias),6) 

    print("Cadenas")
    for i in range(0,matriz_ordenada.shape[0]):
        fila=[] 
        for j in range(0,matriz_ordenada.shape[1]):
            fila.append(str(matriz_ordenada[i,j]))
        print(fila) 

    """
                      
    return (matriz_ordenada,mayores_frecuencias)


###################################################################################
# Función que obtiene una matriz con los números que salieron el sábado/miércoles,#
# el mes dado y la semana dada.                                                   # 
###################################################################################
def obtiene_matriz_datos_dia_mes_semana(dia,vector_dias,mes,vector_meses,semana,vector_semanas,matriz_datos):
    matriz=[]
    nro_filas=0
    vector_de_datos=[]
    for i in range(0,len(vector_dias)):
        if (vector_dias[i] == dia and vector_meses[i][5:7] == mes and vector_semanas[i] == semana):        
            nro_filas=nro_filas + 1
            for k in range(0,6):
                vector_de_datos.append(matriz_datos[i,k])

    filas=nro_filas
    columnas=6
    
    matriz=np.array(vector_de_datos).reshape(filas,columnas)
    #print(matriz)          
    
    return(matriz)
###################################################################################
# Función que obtiene una matriz con los números que salieron el sábado/miércoles #
# y mes dado.                                                   # 
###################################################################################
def obtiene_matriz_datos_dia_mes(dia,vector_dias,mes,vector_meses,matriz_datos):
    matriz=[]
    nro_filas=0
    vector_de_datos=[]
    for i in range(0,len(vector_dias)):
        if (vector_dias[i] == dia and vector_meses[i][5:7] == mes):        
            nro_filas=nro_filas + 1
            for k in range(0,6):
                vector_de_datos.append(matriz_datos[i,k])

    filas=nro_filas
    columnas=6
    
    matriz=np.array(vector_de_datos).reshape(filas,columnas)
    #print(matriz)          
    
    return(matriz)
#######################################################################################################################################################
"""
control_filas=1
nro_filas=10
(matriz_de_datos,tipo_loteria,cadena_fecha_jugada,cadena_dia_semana,semana_del_ayo,semana_del_mes,b1,b2,b3,b4,b5,b6)=lee_datos(control_filas,nro_filas)

print(cadena_fecha_jugada)
print(cadena_dia_semana)
print(semana_del_ayo)
print(semana_del_mes)
print(b1)
print(b6)
"""
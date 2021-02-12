# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:49:33 2020

@author: Luciano
"""
import numpy as np
from itertools import combinations


###########################################################################################
## Función que obtiene todas las posibles combinaciones de subconjuntos de números de    ##
## un vector.                                                                            ##
###########################################################################################
def obtiene_matriz_combinaciones(vector,tamano_subconjuntos):
    combinaciones = combinations(vector,tamano_subconjuntos)
    vector_nuevo=[]
    filas=0
    for i in list(combinaciones):
        vector_nuevo.append(i)
        #print(i)
        filas=filas + 1  
    
    columnas=tamano_subconjuntos
    matriz_combinaciones=np.array(vector_nuevo).reshape(filas,columnas)
    matriz=np.zeros((filas,len(vector)), dtype=int,order='C')
    for i in range(0,matriz_combinaciones.shape[0]):
        for j in range(0,matriz_combinaciones.shape[1]):
            matriz[i,j]=matriz_combinaciones[i,j]
              
    return (matriz,matriz_combinaciones)


###########################################################################################
## Función que obtiene las N ocurrencias más altas en todo el conjunto.                  ##
###########################################################################################
def obtiene_las_N_mayores_frecuencias(N,frecuencias):
    
    mayores_frecuencias=[]
    posiciones=np.zeros(len(frecuencias), dtype=int,order='C')
    #print(posiciones)
    for i in range(0,N):
        if (np.max(frecuencias) != -1): 
            mayores_frecuencias.append(np.max(frecuencias))
            #print(mayores)
            posicion=np.where(frecuencias == np.max(frecuencias))
            #print("Posición encontrada: ",posicion)
    
            posiciones[posicion]= posicion
            #print("Posiciones: ",posiciones)
            
            frecuencias[posicion]=-1
            #print("paso: ",i+1)
            #print(frecuencias)


    #print("Mayores: ",mayores_frecuencias)
    #print("Frecuencias finales: ",frecuencias)
    
    ########
    """
    print("Las frecuencias: ",frecuencias)
    mayores_frecuencias=[]
    for i in range(0,N):
        print("Paso: ",i+1)
        mayores_frecuencias.append(np.max(frecuencias))
        frecuencia_mayor=np.max(frecuencias)
        for j in range(0,len(frecuencias)):
            if(frecuencias[j]==frecuencia_mayor):
                print("Frecuencia a eliminar: ",frecuencias[j])
                frecuencias[j]=-1

        print("Las frecuencias: ",frecuencias)        
                
               
    print("Las frecuencias: ",frecuencias)

    """
    ######   
    return (mayores_frecuencias)
###########################################################################################
## Función que obtiene las N ocurrencias más bajas en todo el conjunto.                  ##
###########################################################################################
def obtiene_las_N_menores_frecuencias(N,frecuencias):
    menores_frecuencias=[]
    posiciones=np.zeros(len(frecuencias), dtype=int,order='C')
    for i in range(0,N):
        if (np.min(frecuencias) != 100000000):
            menores_frecuencias.append(np.min(frecuencias))
            posicion=np.where(frecuencias == np.min(frecuencias))
            posiciones[posicion]= posicion
            frecuencias[posicion]=100000000 
    return (menores_frecuencias)


###########################################################################################
## Función que obtiene los números que corresponden a las N ocurrencias más altas/bajas. ##
###########################################################################################
def obtiene_numeros_con_N_ocurrencias_mas_altas_o_bajas(los_numeros,frecuencias_altas_bajas,frecuencias):
    frecuencia_y_numeros=np.zeros((len(frecuencias_altas_bajas),len(frecuencias) +1), dtype=int,order='C')
    k=0
    for i in frecuencias_altas_bajas:
        frecuencia_y_numeros[k,0]=i
        t=0
        for j in frecuencias:
            if (i == j):
                frecuencia_y_numeros[k,t+1]=los_numeros[t]
            t=t+1
        k=k+1    
    
    print("Las frecuencias mas altas: ",frecuencias_altas_bajas)
    print("Las frecuencias: ",frecuencias)
    print(frecuencia_y_numeros)
    
    listado_frecuencias=[]
    listado_numeros=[]

    for i in range(0,frecuencia_y_numeros.shape[0]):
        for j in range(1,frecuencia_y_numeros.shape[1]):    
            if (frecuencia_y_numeros[i,j] != 0):
                listado_frecuencias.append(frecuencia_y_numeros[i,0])
                listado_numeros.append(frecuencia_y_numeros[i,j])  
     
    return (listado_frecuencias,listado_numeros)

###########################################################################################
"""
vector=[13,	16,	22,	29,	32,	36]
tamano_subconjuntos=4
(matriz,matriz_combinaciones)=obtiene_matriz_combinaciones(vector,tamano_subconjuntos)
print("Matriz de combinaciones: ",matriz_combinaciones )
print("Matriz resultante: ",matriz)
print("Imprimir una fila")
print(matriz[14])
"""

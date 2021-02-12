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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def generar_pdf(dia,mes):
    c = canvas.Canvas("C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/posibles_jugadas.pdf", pagesize=letter)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 13)
    c.drawString(60,740,'POSIBLES JUGADAS PARA HOY: ')
    if (dia=="Sábados"):
        c.drawString(267,740,"Sábado")
    else:
        c.drawString(267,740,"Miércoles")
        

    fecha= datetime.now()
    month=format(fecha.month)
    year=format(fecha.year)
    day=format(fecha.day)
            
                 
    c.drawString(400,740,day +"/" + month +"/"+year)
    c.line(400,737,460,737)
    
    c.setFont('Helvetica', 10)
    c.drawString(30,700,'LOS 6 MAS SALIDORES')
    c.line(30,697,142,697)
    c.drawString(30,680,'NÚMERO')
    c.drawString(100,680,'FRECUENCIA')
    
    archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/resultados/"
    archivo= archivo + "archivo_todas_jugadas_ordenados_frecuencia.csv"       
    
    with open(archivo,encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:           
            if (i<=6):
                #print(row['Número'], row['Frecuencia'])
                x=10*i
                c.drawString(40,677 - x,row['Número'])
                c.drawString(120,677- x,row['Frecuencia'])
                i=i+1
            else:
                 break
            

    
    c.drawString(30,580,'LOS 6 MAS SALIDORES DEL ')
    if (dia=="Sábados"):
        c.drawString(170,580,"Sábado")
    else:
        c.drawString(170,580,"Miércoles")
   
    c.line(30,577,213,577)
    c.drawString(30,560,'NÚMERO')
    c.drawString(100,560,'FRECUENCIA')
    
    if (dia=="Miércoles"):
        el_dia="miercoles"
    if (dia=="Sábados"):
        el_dia="sabados"    
    archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/resultados_solo_"+ el_dia +".csv"    
          
    with open(archivo,encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:
            if (i<=6):
                #print(row['Número'], row['Frecuencia'])
                x=10*i
                c.drawString(40,557 - x,row['Número'])
                c.drawString(120,557- x,row['Frecuencia'])
                i=i+1
            else:
                 break
    
    c.drawString(30,460,'LOS 6 MAS SALIDORES DE ')
    c.drawString(170,460,mes)
    c.line(30,457,213,457)
    c.drawString(30,440,'NÚMERO')
    c.drawString(100,440,'FRECUENCIA')
    archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/archivo_" + mes +".csv"    
           
    with open(archivo,encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:
            if (i<=6):
                #print(row['Número'], row['Frecuencia'])
                x=10*i
                c.drawString(40,437 - x,row['Número'])
                c.drawString(120,437- x,row['Frecuencia'])
                i=i+1
            else:
                 break
    
    c.drawString(30,334,'LOS 6 MAS SALIDORES DE LOS')
    c.drawString(185,334,dia)
    c.drawString(230,334,"de")
    c.drawString(245,334,mes)
    c.line(30,331,270,331)
    c.drawString(30,314,'NÚMERO')
    c.drawString(100,314,'FRECUENCIA')
    
    if (dia=="Sábados"):
        dia="Sábado"
    archivo="C:/Users/58414/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/archivo_"+ dia + "_" + mes +".csv"    
      
           
    with open(archivo,encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:            
            if (i<=6):
                #print(row['Número'], row['Frecuencia'])
                x=10*i
                c.drawString(40,311 - x,row['Número'])
                c.drawString(120,311- x,row['Frecuencia'])
                i=i+1
            else:
                 break
            
            

    c.save()
    
    
    
    return
      
#generar_pdf("Miércoles","enero")    
    
    

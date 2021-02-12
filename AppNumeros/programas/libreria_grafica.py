# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:27:06 2020

@author: Luciano
"""

import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

###########################################################################################
## Función que grafica un vector Y vs un vector X.                                       ##
###########################################################################################
def grafica_en_ventana_general(vectorx,vectory,leyenda_x,leyenda_y,titulo):
    fig, ax1 = plt.subplots(figsize=(5,4), dpi=100)
  
    ax1.set_title(titulo,color="red", fontsize=12)
    ax1.set_ylabel(leyenda_y)
    ax1.set_xlabel(leyenda_x)

    for i in vectorx:                     
        x=[i,i]
        y=[0,vectory[i-1]]
        ax1.plot(x,y,"b-", linewidth=2.5)
        #ax1.bar(x, y, facecolor='red', edgecolor='white')
    
    
    root = tkinter.Tk()
    root.wm_title("Lotto Texas Project")
    root.iconbitmap('logo_1.ico')
    
    #------------------------------CREAR GRAFICA---------------------------------
    #fig = Figure(figsize=(5, 4), dpi=100)    
    canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
    toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    

    tkinter.mainloop()     

    return 
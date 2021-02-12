from django.shortcuts import render, HttpResponse
from django.http import FileResponse, Http404

# Create your views here.
from .programas.generacion_numeros_y_frecuencias import calcula_frecuencias
from .programas.generacion_dia_mes_numeros_y_frecuencias import frecuencias_dia_mes
from .programas.receptor import calcula_frecuencias_dia
from .programas.receptor_mes import calcula_frecuencias_de_los_meses,calcula_frecuencias_mes
from .programas.generar_pdf_hoy import generar_pdf
import csv 
from datetime import datetime

  
    
def recibeDia(request):

    return render(request,"AppDia/diafrecuencia.html") 

    
def receptorDia(request):
    dia_recibido= request.POST['dia']
    calcula_frecuencias_dia(dia_recibido)
    try:
        #return FileResponse(open('C:/Users/Luciano/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/resultados/archivo_pdf.pdf', 'rb'), content_type='application/pdf')
        if (dia_recibido=="Miércoles"):
            el_dia="miercoles"
        if (dia_recibido=="Sábado"):
            el_dia="sabados"
        
        archivo = open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/resultados_solo_'+ el_dia +'.csv', 'rb')
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename='"datos_" + el_dia + ".csv"''
        return response
        
    except FileNotFoundError:
        raise Http404("No se abrió el archivo")


def recibeMes(request):

    return render(request,"AppDia/mesesfrecuencia.html") 

def receptorActividadMes(request):
    actividad_recibida= request.POST['actividad']
    if (actividad_recibida=="1"):
        return render(request,"AppDia/seleccionar_mes.html") 
    else:
        calcula_frecuencias_de_los_meses()
        frase="Se calcularon las frecuencias de todos los meses"
        return render(request,"AppDia/respuesta_mes.html",{"frase":frase})
       
   
def receptorMes(request):
         
    mes_consultado= int(request.POST['mes'])
    calcula_frecuencias_mes(mes_consultado)
    if (mes_consultado==1):
        el_mes="enero"   
                   
    if (mes_consultado==2):
        el_mes="febrero"

    if (mes_consultado==3):
        el_mes="marzo"

    if (mes_consultado==4):
        el_mes="abril"

    if (mes_consultado==5):
        el_mes="mayo"

    if (mes_consultado==6):
        el_mes="junio"

    if (mes_consultado==7):
        el_mes="julio"

    if (mes_consultado==8):
        el_mes="agosto"

    if (mes_consultado==9):
        el_mes="septiembre"

    if (mes_consultado==10):
        el_mes="octubre"

    if (mes_consultado==11):
        el_mes="noviembre"

    if (mes_consultado==12):
        el_mes="diciembre"
    
    try:
        #return FileResponse(open('C:/Users/Luciano/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/resultados/archivo_pdf.pdf', 'rb'), content_type='application/pdf')

        
        
        archivo = open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/archivo_'+ el_mes +'.csv', 'rb')
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename='"datos_" + el_mes + ".csv"''
        return response
        
    except FileNotFoundError:
        raise Http404("Estoy entrando aquí")

    
def recibeDiaMes(request):

    return render(request,"AppDia/diamesfrecuencia.html") 

    
def receptorDiaMes(request):
    dia= request.POST['dia']
    fecha= datetime.now()
    mes=int(format(fecha.month))
    
    frecuencias_dia_mes()
    el_mes=obtiene_mes(mes)
    #documento="Por acá voy"

    try:
        archivo = open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/archivo_'+ dia + '_' + el_mes +'.csv', 'rb')   
           
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename='"datos_" + dia + '_'+ el_mes + ".csv"''
        return response
        
    except FileNotFoundError:
        raise Http404("Estoy entrando aquí") 

    #return HttpResponse(documento)

   
def obtiene_mes(mes_consultado):
    if (mes_consultado==1):
        el_mes="enero"   
                   
    if (mes_consultado==2):
        el_mes="febrero"

    if (mes_consultado==3):
        el_mes="marzo"

    if (mes_consultado==4):
        el_mes="abril"

    if (mes_consultado==5):
        el_mes="mayo"

    if (mes_consultado==6):
        el_mes="junio"

    if (mes_consultado==7):
        el_mes="julio"

    if (mes_consultado==8):
        el_mes="agosto"

    if (mes_consultado==9):
        el_mes="septiembre"

    if (mes_consultado==10):
        el_mes="octubre"

    if (mes_consultado==11):
        el_mes="noviembre"

    if (mes_consultado==12):
        el_mes="diciembre"
        
        
    print("El mes:  ",el_mes)    
    return (el_mes)    
   
def masReportes(request):

    return render(request,"AppDia/reportes_adicionales.html")

def reportesAdicionales(request):
    indice= int(request.POST['reporte'])
    if (indice ==1 or indice == 6 or indice == 11 ):
        tamano_secuencia="2"
    if (indice ==2 or indice == 7 or indice == 12 ):
        tamano_secuencia="3"
    if (indice ==3 or indice == 8 or indice == 13 ):
        tamano_secuencia="4"    
    if (indice ==4 or indice == 9 or indice == 14 ):
        tamano_secuencia="5"
    if (indice ==5 or indice == 10 or indice == 15 ):
        tamano_secuencia="6" 
    if (1<=indice<=5):
        dia=""
    if (6<=indice<=10):
        dia="sabado"
    if (11<=indice<=15):
        dia="miercoles"     
    
    try:
        if (dia==""):
            return FileResponse(open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppNumeros/programas/resultados/archivo_csv_' + tamano_secuencia +'.pdf', 'rb'), content_type='application/pdf')
        else:
            return FileResponse(open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppNumeros/programas/resultados/' + dia + '_archivo_csv_' + tamano_secuencia +'.pdf', 'rb'), content_type='application/pdf')
                                    
        #return FileResponse(open('C:/Users/Luciano/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/archivo_pdf.pdf', 'rb'), content_type='application/pdf')
       
        """
        archivo = open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/dia_'+ dia + '_' + el_mes +'.csv', 'rb')   
           
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename='"datos_" + dia + '_'+ el_mes + ".csv"''
        return response
        """
        
    except FileNotFoundError:
        raise Http404("Estoy entrando aquí") 
        
def llamaPdfHoy(request):
    return render(request,"AppDia/construye_pdf_hoy.html")
    
def obtienePdfHoy(request):
    dia= request.POST['dia']
    fecha= datetime.now()
    mes=int(format(fecha.month))

    el_mes=obtiene_mes(mes)
    generar_pdf(dia,el_mes)
    try:
        return FileResponse(open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppDia/programas/resultados/posibles_jugadas.pdf', 'rb'), content_type='application/pdf')
        
    except FileNotFoundError:
        raise Http404("No se puede abrir el archivo") 
        
def descargarLotto(request):
    return render(request,'https://www.txlottery.org/export/sites/lottery/Games/Lotto_Texas/Winning_Numbers/lottotexas.csv')       
        
def acercaDe(request):
    return render(request,'AppDia/acerca_de.html') 
def Help(request):
    return render(request,'AppDia/help.html')         

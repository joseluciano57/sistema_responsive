from django.shortcuts import render, HttpResponse
from django.http import FileResponse, Http404

# Create your views here.
from .programas.generacion_numeros_y_frecuencias import calcula_frecuencias
import csv 
import pdfkit

def numerosfrecuencia(request):
    calcula_frecuencias()
    try:
        #return FileResponse(open('C:/Users/Luciano/Django_curso/proyectosdjango/LoteriaResponsive/AppNumeros/programas/resultados/archivo_pdf.pdf', 'rb'), content_type='application/pdf')

        archivo = open('C:/Users/58414/Django_curso/proyectosdjango/LoteriaResponsive/AppNumeros/programas/resultados/archivo_todas_jugadas_ordenados_frecuencia.csv', 'rb')
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename="deMayoraMenorFrecuencia.csv"'
        return response
        

    except FileNotFoundError:
        raise Http404()
    #return render(request,"AppNumeros/numerosfrecuencia.html")


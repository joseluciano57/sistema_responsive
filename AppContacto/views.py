from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail
from django.conf import settings

    
def contacto(request):
    formulario_contacto=FormularioContacto()
    if (request.method=="POST"):
       formulario_contacto=FormularioContacto(data=request.POST)
       if formulario_contacto.is_valid():
           asunto=request.POST.get("asunto")
           email=request.POST.get("email")
           mensaje=request.POST.get("mensaje")
           mensaje = email + "  " +  mensaje
           email_from=settings.EMAIL_HOST_USER
           recipient_list=["jlmaldonaj@gmail.com"]
           send_mail(asunto,mensaje,email_from,recipient_list)
           return redirect("/AppContacto/?valido")
        

    return render(request,"AppContacto/contacto.html",{"miformulario":formulario_contacto}) 

"""    
def receptorDia(request):
    dia_recibido= request.POST['dia']
    calcula_frecuencias_dia(dia_recibido)
    try:
        #return FileResponse(open('C:/Users/Luciano/Django_curso/proyectosdjango/ProyectoLoteria/AppNumeros/programas/resultados/archivo_pdf.pdf', 'rb'), content_type='application/pdf')
        if (dia_recibido=="Miércoles"):
            el_dia="miercoles"
        if (dia_recibido=="Sábado"):
            el_dia="sabados"
        
        archivo = open('C:/Users/Luciano/Django_curso/proyectosdjango/ProyectoLoteria/AppDia/programas/resultados/resultados_solo_'+ el_dia +'.csv', 'rb')
        response = FileResponse(archivo, content_type='text/csv')
        response["Content-Disposition"] = 'attachment; filename='"datos_" + el_dia + ".csv"''
        return response
        
    except FileNotFoundError:
        raise Http404("No se abrió el archivo")

"""


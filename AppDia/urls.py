"""proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recibedia/', views.recibeDia, name="recibeDia"),
    path('receptordia/(dia)', views.receptorDia, name="receptorDia"),
    path('recibemes/', views.recibeMes, name="recibeMes"),
    path('recibeactividadmes/(actividad)', views.receptorActividadMes, name="receptorActividadMes"),
    path('receptormes/(mes)', views.receptorMes, name="receptorMes"),
    path('recibediames/', views.recibeDiaMes, name="recibeDiaMes"),
    path('receptordiames/(dia)', views.receptorDiaMes, name="receptorDiaMes"),
    path('masreportes/', views.masReportes, name="masReportes"),
    path('reportesadicionales/(reporte)', views.reportesAdicionales, name="reportesAdicionales"),
    path('llamapdfdia/', views.llamaPdfHoy, name="llamaPdfHoy"),
    path('obtienepdfhoy/(dia)', views.obtienePdfHoy, name="obtienePdfHoy"),
    path('descargas/', views.descargarLotto, name="descargarLotto"),
    path('acercade/', views.acercaDe, name="acercaDe"),
    path('help/', views.Help, name="Help"),
    ]


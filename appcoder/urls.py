from django.urls import path

from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    #path("cargar/procesador/", cargar_procesador, name="formulario_procesadores"),
    path("cargar/placas/", cargar_placas_de_video, name="formulario_placas"),
    path("cargar/ram/", cargar_rams, name="formulario_rams"),
    path("buscar/procesador/", buscar_procesador, name="buscar-procesador"),
    path("busqueda/procesador/", buscar_procesador, name="busqueda_procesador"),
    path("procesadores/", procesadores, name="procesadores"),
]
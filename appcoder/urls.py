from django.urls import path

from appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("cargar/procesador/", cargar_procesador, name="formulario_procesadores"),
    path("cargar/placas/", cargar_placas_de_video, name="formulario_placas"),
    path("cargar/ram/", cargar_rams, name="formulario_rams"),
]
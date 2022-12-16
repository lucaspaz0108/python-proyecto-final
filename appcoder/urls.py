from django.urls import path

from appcoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    #path("cargar/procesador/", cargar_procesador, name="formulario_procesadores"),
    path("cargar/placas/", cargar_placas_de_video, name="formulario_placas"),
    path("cargar/ram/", cargar_rams, name="formulario_rams"),
    path("buscar/procesador/", buscar_procesador, name="buscar-procesador"),
    path("busqueda/procesador/", buscar_procesador, name="busqueda_procesador"),
    path("procesadores/", procesadores, name="procesadores"),
    path("procesadores/eliminar/<id>", eliminar_procesador, name="borrar_procesador"),
    path("procesadores/editar/<id>", editar_procesador, name="editar_procesador"),
    
    path("rams/", RamList.as_view(), name="lista_ram"),
    path("rams/detalle/<pk>/", RamDetail.as_view(), name="detalle_ram"),
    path("rams/crear/", RamCreate.as_view(), name="crear_ram"),
    path("rams/actualizar/<pk>/", RamUpdate.as_view(), name="actualizar_ram"),
    path("rams/borrar/<pk>/", RamDelete.as_view(), name="borrar_ram"),

    path("login/", inicio_sesion, name="auth-login"),
    path("register/", register, name="auth-register"),
    path("logout/", LogoutView.as_view(template_name="appcoder/logout.html"), name="auth-logout")
]
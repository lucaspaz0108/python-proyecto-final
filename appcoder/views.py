from django.shortcuts import render
from appcoder.models import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render (request, "appcoder/base.html")

def cargar_procesador(request):
    if request.method == "POST":
        nombre_procesador = request.POST["procesador"]
        numero_nucleos = request.POST["nucleos"]
        nombre_marca = request.POST["marca"]
        valor_precio = request.POST["precio"]
        procesador = Procesadores(nombre=nombre_procesador, nucleos=numero_nucleos, marca=nombre_marca, precio=valor_precio)
        procesador.save()
    

    return render(request, "appcoder/procesador_formulario.html")

def cargar_placas_de_video(request):
    if request.method == "POST":
        nombre_placa = request.POST["placa"]
        numero_vram = request.POST["vram"]
        nombre_marca = request.POST["marca"]
        valor_precio = request.POST["precio"]
        procesador = PlacasDeVideo(nombre=nombre_placa, VRAM=numero_vram, marca=nombre_marca, precio=valor_precio)
        procesador.save()
    

    return render(request, "appcoder/placas_formulario.html")

def cargar_rams(request):
    if request.method == "POST":
        nombre_memoria = request.POST["modelo"]
        numero_ram = request.POST["ram"]
        nombre_marca = request.POST["marca"]
        valor_precio = request.POST["precio"]
        procesador = RAM(nombre=nombre_memoria, RAM=numero_ram, marca=nombre_marca, precio=valor_precio)
        procesador.save()
    

    return render(request, "appcoder/ram_formulario.html")

def buscar_procesador(request):
    if request.GET:
        procesadores = Procesadores.objects.filter(nombre__icontains=request.GET["nombre"])
        return render(request, "appcoder/busqueda_procesador.html", {"listado_procesadores": procesadores})
    return render (request, "appcoder/busqueda_procesador.html", {"listado_procesadores": []})

#     return render (request, "appcoder/busqueda_procesador.html")

# def buscar(request):
#     if request.GET["procesador"]:
#         procesador = request.GET:
#         procesadores = Procesadores.objects.filter(nombre__icontains=procesador)

#         return render (request, "appcoder/resultados_busqueda_procesador.html", {"procesadores": procesadores})
#     else:
#         respuesta = "No enviaste datos"
    
#     return HttpResponse(respuesta)
 #respuesta = f"Estoy buscando al procesador: {request.GET['procesador']}"
# def resultados_busqueda_cursos(request):
#     nombre_procesador = request.GET["nombre_procesador"]
#     procesadores = Procesadores.objects.filter(nombre__icontains=procesador)

#     return render (request, "appcoder/resultados_busqueda_procesador.html", {"procesadores": procesadores})
from django.shortcuts import render, redirect
from appcoder.models import *
from django.http import HttpResponse
from appcoder.forms import  ProcesadorFormulario, UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render (request, "appcoder/base.html", {"imagen_url":imagen_url})

"""def cargar_procesador(request):
    if request.method == "POST":
        nombre_procesador = request.POST["procesador"]
        numero_nucleos = request.POST["nucleos"]
        nombre_marca = request.POST["marca"]
        valor_precio = request.POST["precio"]
        procesador = Procesadores(nombre=nombre_procesador, nucleos=numero_nucleos, marca=nombre_marca, precio=valor_precio)
        procesador.save()
    

    return render(request, "appcoder/procesador_formulario.html")"""

def procesadores (request):

    errores = ""

    if request.method == "POST":
        formulario = ProcesadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            procesador = Procesadores(nombre=data["nombre"], nucleos=data["nucleos"], marca=data["marca"], precio=data["precio"])
            procesador.save()
        else:
            errores = formulario.errors

    procesadores = Procesadores.objects.all()
    formulario = ProcesadorFormulario()

    contexto = {"listado_procesadores": procesadores, "formulario": formulario, "errores": errores}
    return render(request, "appcoder/procesadores.html", contexto)

@login_required
def editar_procesador(request, id):
    procesador = Procesadores.objects.get(id=id)

    if request.method == "POST":
        formulario = ProcesadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            procesador.nombre = data["nombre"]
            procesador.nucleos = data["nucleos"]
            procesador.marca = data["marca"]
            procesador.precio = data["precio"]
            procesador.save()
            return redirect("procesadores")
        else:
            return render(request, "appcoder/editar_procesador.html", {"formulario": formulario, "errores": formulario.errors})
    else: 
        formulario = ProcesadorFormulario(initial={"nombre":procesador.nombre, "nucleos":procesador.nucleos, "marca":procesador.marca, "precio":procesador.precio})
        return render(request, "appcoder/editar_procesador.html", {"formulario": formulario, "errores": ""})
    


@login_required
def eliminar_procesador(request, id):
    procesador = Procesadores.objects.get(id=id)
    procesador.delete()

    return redirect("procesadores")


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

class RamList(ListView):

    model = RAM
    template_name = "appcoder/list_ram.html"


class RamDetail(DetailView):
    model = RAM
    template_name = "appcoder/detail_ram.html"

class RamCreate(LoginRequiredMixin ,CreateView):

    model = RAM
    success_url = "appcoder/ram_form.html"
    fields = ["nombre", "RAM", "marca", "precio"]
    template_name = "appcoder/ram_form.html"

class RamUpdate(UpdateView):
    
    model = RAM
    success_url = "appcoder/rams/"
    fields = ["nombre", "RAM", "marca", "precio"]

class RamDelete(LoginRequiredMixin ,DeleteView):
    model = RAM
    success_url = "appcoder/rams/"



def inicio_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "appcoder/login.html", {"form":formulario, "errors":"Credencial Inválida"})
        else:
            return render(request, "appcoder/login.html", {"form":formulario, "errors": formulario.errors})
        

    formulario = AuthenticationForm()
    return render (request, "appcoder/login.html", {"form": formulario, "errors":errors})


def register(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "appcoder/register.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = UserRegisterForm()
    return render(request, "appcoder/register.html", {"form": formulario})


@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        #cargar informacion en el formulario
        formulario = UserEditForm(request.POST)
        #validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data
        #actualizacion del usuario con los datos del form
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            
            usuario.save()
            return redirect("inicio")
        else:
            return render(request, "appcoder/editar_perfil.html", {"form": formulario, "errors":formulario.errors})
    else:
        #crear formulario vacío
        formulario = UserEditForm(initial = {"email":usuario.email,"first_name": usuario.first_name, "last_name": usuario.last_name})
        pass
    return render(request, "appcoder/editar_perfil.html",{"form":formulario})


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            
            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()
            
            return redirect("inicio")
        else:
            return render(request, "appcoder/agregar_avatar.html", {"form": formulario, "errors":formulario.errors})
        
    formulario = AvatarForm()
    
    return render(request, "appcoder/agregar_avatar.html", {"form": formulario})
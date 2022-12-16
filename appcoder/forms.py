from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProcesadorFormulario(forms.Form):
    nombre = forms.CharField()
    nucleos = forms.IntegerField()
    marca = forms.CharField()
    precio = forms.IntegerField()

class PlacasDeVideoFormulario(forms.Form):
    nombre = forms.CharField()
    VRAM = forms.IntegerField()
    marca = forms.CharField()
    precio = forms.IntegerField()

class RAMFormulario(forms.Form):
    nombre = forms.CharField()
    RAM = forms.IntegerField()
    marca = forms.CharField()
    precio = forms.IntegerField()

"""class FormularioProcesador(forms.Form):
    nombre = forms.CharField()
    nucleos = forms.IntegerField()
    marca = forms.CharField()
    precio = forms.IntegerField()"""
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

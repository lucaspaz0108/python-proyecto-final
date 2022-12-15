from django import forms

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
    precio = forms.IntegerField()"""""

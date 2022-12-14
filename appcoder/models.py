from django.db import models
from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
# Create your models here.

class Procesadores(models.Model):
    nombre = models.CharField(max_length=50)
    nucleos = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} -> Precio: {self.precio} "

class PlacasDeVideo(models.Model):
    nombre = models.CharField(max_length=50)
    VRAM = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre} -> VRAM: {self.VRAM} "

    

class RAM(models.Model):
    nombre = models.CharField(max_length=50)
    RAM = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} -> Nombre: {self.nombre} "
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
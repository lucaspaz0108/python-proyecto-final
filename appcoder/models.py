from django.db import models
from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH

# Create your models here.

class Procesadores(models.Model):
    nombre = models.CharField(max_length=50)
    nucleos = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()

class PlacasDeVideo(models.Model):
    nombre = models.CharField(max_length=50)
    VRAM = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()

class RAM(models.Model):
    nombre = models.CharField(max_length=50)
    RAM = models.IntegerField()
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
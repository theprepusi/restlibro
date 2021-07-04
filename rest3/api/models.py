from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)


class Cuenta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
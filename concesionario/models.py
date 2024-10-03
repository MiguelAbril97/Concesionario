from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Vendedor(models.Model):
    jefe=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    numeroVentas = models.IntegerField()
    fecha_contrato = models.DateTimeField()

class Coche(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_entrada = models.DateTimeField()

class Venta(models.Model):
    fecha_venta = models.DateTimeField(default=timezone.now)
    vendedor = models.CharField(max_length=50)
    coche_vendido=models.CharField(max_length=50)
    precio = models.PositiveIntegerField(default=0)


from django.db import models
from core.user.models import User
import datetime

class Client(models.Model):
    dni = models.CharField(max_length=9, verbose_name='dni')
    nombre = models.CharField(max_length=40, verbose_name='nombre')
    apellidos = models.CharField(max_length=60, verbose_name='apellidos')
    direccion = models.CharField(max_length=150, verbose_name='direccion')
    fechaNacimiento = models.DateField(verbose_name='fechaNacimiento')
    fechaAlta = models.DateField(verbose_name='fechaAlta', default= datetime.date.today())
    activo = models.BooleanField(verbose_name='activo', default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="idUsuario")

    def __str__(self):
        return self.nombre + " " + self.apellidos

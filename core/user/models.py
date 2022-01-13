from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# class Usuario(models.Model):
#     username = models.CharField(max_length=40, verbose_name='username')
#     password = models.CharField(max_length=255, verbose_name='password')

#     def __str__(self):
#         return self.username

class User(AbstractUser):
    is_client = models.BooleanField(verbose_name='is_client', default=False)
    dni = models.CharField(max_length=9, verbose_name='dni',unique = True, default='No', blank = False, null = False)
    direccion = models.CharField(max_length=150, verbose_name='direccion', null = False)
    fechaNacimiento = models.DateField(null=True, verbose_name='fechaNacimiento')
    biografia = models.CharField(max_length=255, null=True, verbose_name='biografia')
  

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + self.username
    

    



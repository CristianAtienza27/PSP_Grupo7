from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.username


    # Guarde el usuario
    # Guarde el cliente 
    



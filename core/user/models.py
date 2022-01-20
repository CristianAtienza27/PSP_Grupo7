from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.username

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)
    # Guarde el usuario
    # Guarde el cliente 
    



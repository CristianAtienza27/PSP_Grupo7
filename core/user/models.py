from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    class UserType(models.TextChoices):
        Client = 'Cliente', ('Cliente')
        Employee = 'Empleado', ('Empleado')
        Admin = 'Administrador', ('Administrador')
        
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=9,verbose_name="DNI")
    nombre=models.CharField(max_length=50,verbose_name="Nombre")
    apellidos=models.CharField(max_length=50,verbose_name="Apellido")
    direccion=models.CharField(max_length=50,verbose_name="Dirección")
    fechaNacimiento=models.DateField(verbose_name="Fecha de cumpleaños",null=True)
    fechaAlta=models.DateTimeField(verbose_name="Fecha de registro", auto_now=True)
    biografia = models.CharField(max_length=400, verbose_name = "Biografía", null=True)
    activo=models.BooleanField(verbose_name="Activo",default=False)
    role_user = models.CharField(max_length=50,verbose_name="role",choices=UserType.choices)
    
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    
    def _str_(self):
        return self.dni+" "+self.nombre+" "+self.apellidos+""+self.fechaNacimiento+" "+self.direccion+"  "+self.activo+" "+self.role_user

    # Guarde el usuario
    # Guarde el cliente 
    



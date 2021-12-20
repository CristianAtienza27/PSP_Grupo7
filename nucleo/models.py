from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# class Usuario(models.Model):
#     username = models.CharField(max_length=40, verbose_name='username')
#     password = models.CharField(max_length=255, verbose_name='password')

#     def __str__(self):
#         return self.username

class User(AbstractUser):
    # is_admin = models.BooleanField(verbose_name='is_admin', default=False)
    is_client = models.BooleanField(verbose_name='is_client', default=False)
    dni = models.CharField(max_length=9, verbose_name='dni',unique = True, default='No', blank = False, null = False)
    nombre = models.CharField(max_length=40, verbose_name='nombre', null = False)
    apellidos = models.CharField(max_length=60, verbose_name='apellidos', null = False)
    direccion = models.CharField(max_length=150, verbose_name='direccion', null = False)
    fechaNacimiento = models.DateField(null=True, verbose_name='fechaNacimiento')
    biografia = models.CharField(max_length=255, null=True, verbose_name='biografia')
    # username = models.CharField(max_length=40, unique=True, verbose_name='username')
    # password = models.CharField(max_length=255, verbose_name='password')
    fechaAlta = models.DateField(verbose_name='fechaAlta', null=True, default=datetime.now)
    activo = models.BooleanField(verbose_name='activo',default=False, null=True)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="idUsuario")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + self.username
    
# class Empleado(models.Model):
#     dni = models.CharField(max_length=9, verbose_name='dni')
#     nombre = models.CharField(max_length=40, verbose_name='nombre')
#     apellidos = models.CharField(max_length=60, verbose_name='apellidos')
#     direccion = models.CharField(max_length=150, verbose_name='direccion')
#     biografia = models.CharField(max_length=255, verbose_name='biografia')
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="idUsuario")

#     def __str__(self):
#         return self.nombre + "  " + self.apellidos + " " + self.usuarios.username
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='nombre')
    foto = models.ImageField(upload_to="photos/", verbose_name="foto")

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='titulo')
    descripcion = models.CharField(max_length=255, verbose_name='descripcion')
    nivel = models.IntegerField(verbose_name='nivel')
    fechaInicio = models.DateField(verbose_name='fechaInicio')
    fechaFin = models.DateField(verbose_name='fechaFin')
    informeFinal = models.CharField(max_length=255, verbose_name='informeFinal')
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='idEmpleado', related_name='empleado')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='idCategoria', related_name='categoria')

    class Meta:
        ordering = ['-fechaInicio']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.titulo
    
class Participa(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='idCliente', related_name='cliente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name='idProyecto', related_name='proyecto')
    fechaInscripcion = models.DateField(verbose_name='fechaInscripcion')
    rol = models.CharField(max_length=100, verbose_name='rol')

    class Meta:
        ordering = ['-fechaInscripcion']
    



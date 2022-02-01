from django.db import models
from core.user.models import User
from core.category.models import Category

class Project(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Título')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción')
    nivel = models.IntegerField(verbose_name='Nivel')
    fechaInicio = models.DateField(verbose_name='Fecha de Inicio')
    fechaFin = models.DateField(verbose_name='Fecha Final')
    informeFinal = models.CharField(max_length=255, verbose_name='informeFinal')
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Empleado', related_name='empleado')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría', related_name='categoria')

    def __str__(self):
        return self.titulo
    
class Participa(models.Model):
    class ParticipaType(models.TextChoices):
        SinRol = 'Sin asignar', ('Sin asignar')
        BackEnd = 'Backend', ('Backend')
        FrontEnd = 'FrontEnd', ('FrontEnd')
        FullStack = 'Fullstack', ('Fullstack')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    proyecto = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto')
    fechaInscripcion = models.DateField(verbose_name='Fecha de inscripción')
    rol = models.CharField(max_length=100,default=ParticipaType.SinRol, verbose_name='Rol', choices=ParticipaType.choices)

    # def __str__(self):
    #     return self.fechaInscripcion + ' ' + self.rol
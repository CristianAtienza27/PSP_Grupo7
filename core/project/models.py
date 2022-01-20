from django.db import models
from core.client.models import Client
from core.employee.models import Employee
from core.category.models import Category

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='titulo')
    descripcion = models.CharField(max_length=255, verbose_name='descripcion')
    nivel = models.IntegerField(verbose_name='nivel')
    fechaInicio = models.DateField(verbose_name='fechaInicio')
    fechaFin = models.DateField(verbose_name='fechaFin')
    informeFinal = models.CharField(max_length=255, verbose_name='informeFinal')
    empleado = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='idEmpleado', related_name='empleado')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='idCategoria', related_name='categoria')

    def __str__(self):
        return self.titulo

class Participa(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='idCliente', related_name='cliente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name='idProyecto', related_name='proyecto')
    fechaInscripcion = models.DateField(verbose_name='fechaInscripcion')
    rol = models.CharField(max_length=100, verbose_name='rol')

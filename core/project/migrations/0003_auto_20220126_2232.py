# Generated by Django 3.1.2 on 2022-01-26 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('project', '0002_auto_20220126_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='category.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='project',
            name='descripcion',
            field=models.CharField(max_length=255, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to=settings.AUTH_USER_MODEL, verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fechaFin',
            field=models.DateField(verbose_name='Fecha Final'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fechaInicio',
            field=models.DateField(verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='project',
            name='nivel',
            field=models.IntegerField(verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='project',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
    ]

# Generated by Django 3.1.2 on 2022-01-20 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('category', '0001_initial'),
        ('client', '0004_auto_20220120_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='titulo')),
                ('descripcion', models.CharField(max_length=255, verbose_name='descripcion')),
                ('nivel', models.IntegerField(verbose_name='nivel')),
                ('fechaInicio', models.DateField(verbose_name='fechaInicio')),
                ('fechaFin', models.DateField(verbose_name='fechaFin')),
                ('informeFinal', models.CharField(max_length=255, verbose_name='informeFinal')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='category.category', verbose_name='idCategoria')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='employee.employee', verbose_name='idEmpleado')),
            ],
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInscripcion', models.DateField(verbose_name='fechaInscripcion')),
                ('rol', models.CharField(max_length=100, verbose_name='rol')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='client.client', verbose_name='idCliente')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto', to='project.proyecto', verbose_name='idProyecto')),
            ],
        ),
    ]

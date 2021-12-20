# Generated by Django 3.1.2 on 2021-12-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_auto_20211220_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='user',
            name='activo',
            field=models.BooleanField(default=False, null=True, verbose_name='activo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(default='No', max_length=9, unique=True, verbose_name='dni'),
        ),
    ]

# Generated by Django 3.1.2 on 2022-01-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20220127_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participa',
            name='rol',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='rol'),
        ),
    ]

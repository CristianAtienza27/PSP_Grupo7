from django.db import models
from rest_framework import serializers
from core.user.models import User
from core.project.models import Project

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre','apellidos','email','fechaNacimiento','fechaAlta','activo','role_user']

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['titulo','descripcion','nivel','fechaInicio','fechaFin','categoria_id','empleado_id']



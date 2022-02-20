from django.db import models
from rest_framework import serializers, viewsets
from core.user.models import User
from core.project.models import Project
from rest_framework.permissions import IsAuthenticated
from core.Api.serializers import ClientSerializer


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['titulo','descripcion','nivel','fechaInicio','fechaFin','categoria_id','empleado_id']



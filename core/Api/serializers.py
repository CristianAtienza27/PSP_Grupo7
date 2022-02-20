from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from core.project.models import Project 
from core.category.models import Category

class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)

    class Meta:
        model = get_user_model()
        fields =  ['nombre','password','username','apellidos','email','fechaNacimiento','fechaAlta','activo','role_user']

class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False)
    password = serializers.CharField(
        min_length=8)

    class Meta:
        model = get_user_model()
        fields =  ('nombre','apellidos','dni','direccion','biografia','username','email','password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('nombre','foto')

class ProjectSerializers(serializers.ModelSerializer):
    titulo = serializers.CharField(required=False)
    descripcion = serializers.CharField(required=False)
    fechaInicio = serializers.DateField(required=False)
    fechaFin = serializers.DateField(required=False)
    empleado =  EmployeeSerializer(read_only=True)
    categoria = CategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['titulo', 'descripcion', 'nivel', 'fechaInicio', 'fechaFin', 'informeFinal', 'empleado', 'categoria']
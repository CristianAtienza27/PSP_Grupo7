from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from core.project.models import Project 
from core.category.models import Category

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =  ['nombre','password','username','apellidos','email','fechaNacimiento','fechaAlta','activo','role_user']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =  ('nombre','apellidos','dni','direccion','biografia','username','email','password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('nombre','foto')

class ProjectSerializers(serializers.ModelSerializer):
    empleado =  EmployeeSerializer(read_only=True)
    categoria = CategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['titulo', 'descripcion', 'nivel', 'fechaInicio', 'fechaFin', 'informeFinal', 'empleado', 'categoria']
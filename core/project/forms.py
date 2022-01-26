from django.forms import *
from core.project.models import Project

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'titulo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el título',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                }
            ),
            'Nivel': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nivel',
                }
            ),
            'fechaInicio': DateInput(
                attrs={
                   'type': 'date'
                }
            ),
            'fechaFin': DateInput(
                attrs={
                   'type': 'date'
                }
            )
                   
        }
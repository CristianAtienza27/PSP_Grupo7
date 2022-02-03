from django.forms import *
from core.project.models import Project, Participa

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['titulo','descripcion','nivel','fechaInicio','fechaFin','categoria']
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
                   'type': 'date',
                },
                format=('%Y-%m-%d')
            ),
            'fechaFin': DateInput(
                attrs={
                   'type': 'date'
                },
                format=('%Y-%m-%d')
            )
                 
        }

        exclude = ['empleado_id']

# class InscriptionForm(ModelForm):
#     class Meta:
#         model = Participa
#         fields = "__all__"

                   

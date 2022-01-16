from django.forms import *
from core.employee.models import Employee

class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ('nombre','apellidos','dni','direccion','biografia')
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su DNI',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'biografia': Textarea(
                attrs={
                    'placeholder': 'Ingrese su biografía',
                }
            )
        }
from django.forms import *
from core.client.models import Client

class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ('nombre','apellidos','dni','direccion','fechaNacimiento')
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
            'fechaNacimiento': DateInput(
                attrs={
                    'placeholder': 'Ingrese su fecha de nacimiento',
                    'type': 'date'
                }
            )
        }
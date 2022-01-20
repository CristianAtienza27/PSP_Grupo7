from django.forms import *
from core.category.models import Category

class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ('nombre','foto')
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'foto': FileInput(
                attrs={
                    'placeholder': 'Ingrese una foto',
                }
            )
        }
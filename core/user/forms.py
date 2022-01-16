from django.forms import *
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm

from core.user.models import User

class UserCreationFormWithUsername(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs['autofocus'] = True

    # username = CharField(widget=TextInput())
    # email = EmailField(widget=EmailInput())
    # password1 = CharField(widget=PasswordInput())
    # password2 = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'password1': PasswordInput(
                attrs={
                    'placeholder': 'Ingrese una contraseña',
                }
            ),
            'password2': PasswordInput(
                attrs={
                    'placeholder': 'Confirme su contraseña',
                }
            )
        }

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user
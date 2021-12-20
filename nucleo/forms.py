from django import forms
from nucleo.models import User

class UserCreate(forms.ModelForm):

    class Meta:
        model = User 
        fields = ['nombre','apellidos','username','email','password','direccion','fechaNacimiento','dni']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class UserCreationForm(UserCreationForm):
    dni = forms.TextInput(attrs={'class':'form-control'}), 
    first_name = forms.TextInput(attrs={'class':'form-control'}),
    last_name = forms.TextInput(attrs={'class':'form-control'}),
    username = forms.TextInput(attrs={'class':'form-control'}),
    email = forms.EmailField(required=True,help_text="Requerido. 254 caracteres maximo")
    password = forms.PasswordInput(attrs={'class':'form-control'}),
    direccion = forms.TextInput(attrs={'class':'form-control'}),

    class Meta:
        model=User
        fields=('username','email','password1','password2','dni','first_name', 'last_name', 'fechaNacimiento', 'direccion')

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save()
        user.email = self.cleaned_data["email"]
        user.dni = self.cleaned_data["dni"]
        user.firs_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.fechaNacimiento = self.cleaned_data["fechaNacimiento"]
        user.direccion = self.cleaned_data["direccion"]
        user.is_cliente = True
        user.is_active= True
        user.save()
        return

    def clean_email(self):
        value=self.cleaned_data['email']
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Este email ya esta en uso, prueba con otro")
        return value
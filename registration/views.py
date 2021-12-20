from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms

# Create your views here.


class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='registration/registro.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb2',
        'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control mb2',
        'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control mb2',
        'placeholder':'Confirmación Contraseña'})
    
        return form
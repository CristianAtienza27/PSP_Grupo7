from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, RedirectView
from django.contrib import messages

import PSP_Grupo7.settings as setting


class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        messages.success(self.request, '¡Bienvenido, ' + self.request.user.username + '!')
        if self.request.user.role_user == 'Cliente':
                 return reverse('project:project_inscription')
        elif self.request.user.role_user == 'Empleado':
                return reverse('project:project_list')
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout con éxito')
        return super().dispatch(request, *args, **kwargs)

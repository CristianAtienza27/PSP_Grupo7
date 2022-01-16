from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.client.forms import ClientForm
from core.user.forms import UserCreationFormWithUsername
from core.user.models import User
from core.client.models import Client
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'create.html'
#     success_url = reverse_lazy('login')
#     url_redirect = success_url

#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Usuario registrado con éxito')
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Nuevo Usuario'
#         context['entity'] = 'Usuarios'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    second_form_class = UserCreationFormWithUsername
    template_name = 'client/create.html'
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        
        context['title'] = 'Nuevo Cliente'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            client = form.save(commit=False)
            client.usuario = form2.save()
            client.save()
            messages.success(request, 'Cliente registrado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ClientUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin,UpdateView):
    model = Client
    form_class = ClientForm
    second_form_class = UserCreationFormWithUsername
    template_name = 'client/create.html'
    permission_required = ('client.change_client')
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid and form2.is_valid():
            client = form.save(commit=False)
            client.idUser = form2.save()
            client.save()
            messages.success(request, 'Cliente eliminado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        
        context['title'] = 'Datos Personales'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context



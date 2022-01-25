from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from core.client.forms import ClientForm
from core.user.forms import UserForm
from core.user.models import User
from core.client.models import Client
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

class ClientListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Client
    template_name = 'client/list.html'
    # permission_required = '.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['clients'] = Client.objects.all()
        context['create_url'] = reverse_lazy('adm:client_create')
        context['entity'] = 'Clientes'
        return context

def ClientActivateView(request,pk):
    Client.objects.filter(pk=pk).update(activo=1)
    messages.success(request, 'Cliente activado con éxito')
    url = reverse('adm:client_list')
    return HttpResponseRedirect(url)

def ClientDeactivateView(request,pk):
    Client.objects.filter(pk=pk).update(activo=0)
    messages.success(request, 'Cliente desactivado con éxito')
    url = reverse('adm:client_list')
    return HttpResponseRedirect(url)

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    second_form_class = UserForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('login')
    url_redirect = success_url

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


class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    form_class = ClientForm
    second_form_class = UserForm
    template_name = 'client/create.html'
    # permission_required = ('client.change_client')
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        client = Client.objects.get(pk=kwargs.get('pk'))

        if form.is_valid and form2.is_valid():
            client = form.save(commit=False)
            client.idUser = form2.save()
            client.save()
            messages.success(request, 'Cliente actualizado con éxito')
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

class ClientDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'client/delete.html'
    success_url = reverse_lazy('adm:client_list')
    # permission_required = 'adm..delete_client'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object.delete()
        messages.success(request, 'Datos modificados con éxito')
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Cliente'
        context['list_url'] = self.success_url
        return context

#Vista de consultar

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.client.forms import ClientForm
from core.user.forms import UserCreationFormWithUsername
from core.user.models import User
from core.client.models import Client
from core.employee.models import Employee
from core.employee.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

class ClientListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Client
    template_name = 'client/list.html'
    # permission_required = '.view_client'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['clients'] = Client.objects.all()
        context['create_url'] = reverse_lazy('adm:client_create')
        context['entity'] = 'Clientes'
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

class EmployeeListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Employee
    template_name = 'employee/list.html'
    # permission_required = '.view_client'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empleados'
        context['clients'] = Employee.objects.all()
        context['create_url'] = reverse_lazy('adm:employee_create')
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    second_form_class = UserCreationFormWithUsername
    template_name = 'client/create.html'
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        
        context['title'] = 'Nuevo Empleado'
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
            messages.success(request, 'Empleado registrado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

    

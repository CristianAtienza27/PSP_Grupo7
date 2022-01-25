from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from core.client.forms import ClientForm
from core.user.forms import UserForm
from core.user.models import User
from core.client.models import Client
from core.employee.models import Employee
from core.employee.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

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
    second_form_class = UserForm
    template_name = 'employee/create.html'
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
            employee = form.save(commit=False)
            employee.usuario = form2.save()
            employee.save()
            messages.success(request, 'Empleado registrado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class EmployeeUpdateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    second_form_class = UserForm
    template_name = 'employee/create.html'
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
        
        context['title'] = 'Editar Empleado'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            employee = form.save(commit=False)
            employee.usuario = form2.save()
            employee.save()
            messages.success(request, 'Empleado registrado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

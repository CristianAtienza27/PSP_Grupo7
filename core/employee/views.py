from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from core.client.forms import ClientForm
from core.user.forms import UserForm
from core.user.models import User
from core.employee.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from core.decorators import *
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

class EmployeeListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = User
    template_name = 'employee/list.html'
    # permission_required = '.view_client'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empleados'
        context['employees'] = User.objects.filter(role_user='Empleado')
        context['create_url'] = reverse_lazy('adm:employee_create')
        return context

@method_decorator(is_admin, name="dispatch")
class EmployeeCreateView(CreateView):
    model = User
    form_class = EmployeeForm
    template_name = 'employee/create.html'
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Nuevo Empleado'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            employee = form.save(commit=False)
            employee.role_user = 'Empleado'
            employee.save()
            messages.success(request, 'Empleado registrado con éxito')
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        messages.success(self.request, 'Empleado registrado con éxito')
        return reverse('adm:employee_list')
    

class EmployeeUpdateView(UpdateView):
    model = User
    form_class = EmployeeForm
    template_name = 'employee/create.html'
    success_url = reverse_lazy('login')
    url_redirect = success_url

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)       
        context['title'] = 'Editar Empleado'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Empleado actualizado con éxito')
        return reverse('adm:employee_list')

class EmployeeDeleteView(DeleteView):
    model = User
    template_name = 'employee/delete.html'
    success_url = reverse_lazy('adm:employee_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Empleado'
        context['list_url'] = self.success_url
        return context

    def get_success_url(self):
        messages.success(self.request, 'Empleado eliminado con éxito')
        return reverse('adm:employee_list')

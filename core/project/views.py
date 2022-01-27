from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from core.client.forms import ClientForm
from core.project.forms import ProjectForm
from core.user.models import User
from core.category.models import Category
from core.project.models import Project, Participa
from core.employee.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

from core.decorators import *
from django.utils.decorators import method_decorator

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    #model = Project
    template_name = 'project/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        context['projects'] = Project.objects.filter(empleado=self.request.user)
        context['create_url'] = reverse_lazy('project:project_create')
        return context
    
    def get_queryset(self):
        return Project.objects.filter(empleado=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Proyecto'
        context['list_url'] = reverse_lazy('project:project_list')
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Proyecto registrado con éxito')
        return reverse('project:project_list')
    
@method_decorator(owns_project, name="dispatch")
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Proyecto'
        context['list_url'] = reverse_lazy('project:project_list')
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Proyecto actualizado con éxito')
        return reverse('project:project_list')

@method_decorator(owns_project, name="dispatch")
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project:project_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Proyecto eliminado con éxito')
        #esto no funciona 
        #return reverse(self.success_url)
        return reverse('project:project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Proyecto'
        context['list_url'] = self.success_url
        return context
    
class ProjectHistoryView(LoginRequiredMixin, DeleteView):
    template_name = 'project/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historial de Proyectos'
        context['projects'] = Project.objects.filter(empleado=self.request.user)
        return context
    
    def get_queryset(self):
        return Project.objects.filter(empleado=self.request.user)

class ProjectInscriptionView(LoginRequiredMixin, ListView):
    model = Participa
    template_name = 'project/listC.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        context['projects'] = Project.objects.all()
        context['create_url'] = reverse_lazy('project:project_inscription')
        return context

def InscriptionCreate(request,pk):
    
    project = Project.objects.filter(pk=pk)
    messages.success(request, 'Cliente activado con éxito')
    url = reverse('project/inscription')
    return HttpResponseRedirect(url)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Listado de Proyectos'
    #     context['projects'] = Project.objects.all()
    #     context['create_url'] = reverse_lazy('project:project_inscription')
    #     return context
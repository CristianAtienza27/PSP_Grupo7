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
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/list.html'
    # permission_required = '.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        context['projects'] = Project.objects.all()
        context['create_url'] = reverse_lazy('project:project_create')
        return context

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

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project:project_list')
    # permission_required = 'adm..delete_client'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Proyecto eliminado con éxito')
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Categoría'
        context['list_url'] = self.success_url
        return context

class ProjectInscriptionView(LoginRequiredMixin, ListView):
    model = Participa
    template_name = 'project/listC.html'
    # permission_required = '.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idProj = []
        inscripciones = Participa.objects.filter(cliente_id=self.request.user.id)
        for insc in inscripciones:
            idProj.append(insc.proyecto.pk)
        projects = Project.objects.exclude(pk__in = idProj)

        context['projects'] = projects
        context['title'] = 'Listado de Proyectos'
        
        context['create_url'] = reverse_lazy('project:project_inscription')
        return context

class ProjectInscriptionView(LoginRequiredMixin, ListView):
    model = Participa
    template_name = 'project/listC.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        idProj = []
        inscripciones = Participa.objects.filter(cliente_id=self.request.user.id)
        for insc in inscripciones:
            idProj.append(insc.proyecto.pk)

        categoria = self.request.GET.get('category', None)
        fechaIni = self.request.GET.get('fechaIni',None)
        fechaFin = self.request.GET.get('fechaFin',None)

        if categoria is not None and fechaIni != '' and fechaFin != '':
            projects = Project.objects.filter(categoria_id=categoria,fechaInicio__lte=fechaIni,fechaFin__gte=fechaFin).exclude(pk__in = idProj)
        elif fechaIni != '' and fechaFin != '':
            projects = Project.objects.filter(fechaInicio=fechaIni).filter(fechaFin=fechaFin).exclude(pk__in = idProj)
        elif categoria is not None and categoria != '0':
            projects = Project.objects.filter(categoria_id=categoria).exclude(pk__in = idProj)
        else:
            projects = Project.objects.filter().exclude(pk__in = idProj)

        context['projects'] = projects
        context['categories'] = Category.objects.all()
        context['title'] = 'Listado de Proyectos'
        
        context['create_url'] = reverse_lazy('project:project_inscription')
        return context    

def InscriptionCreate(request,pk):
    project = Project.objects.filter(pk=pk).first()

    if project is not None:
        inscripcion = Participa()
        inscripcion.cliente = request.user
        inscripcion.proyecto = project
        inscripcion.fechaInscripcion = datetime.today()
        inscripcion.save()

        messages.success(request, 'Inscripción en proyecto con éxito')
    else:
        messages.success(request, 'Error al realizar la inscripción')
    
    url = reverse('project:project_inscription')
    return HttpResponseRedirect(url)

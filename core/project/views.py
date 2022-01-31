from datetime import datetime
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
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

from core.decorators import *
from django.utils.decorators import method_decorator

#UTIL: https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
#Para las consultas : https://docs.djangoproject.com/en/4.0/ref/models/querysets

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    page_kwarg = 'page'
    status_kwarg = 'status'
    model = Project
    ordering = ['id']
    template_name = 'project/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        context['projects'] = Project.objects.filter(empleado=self.request.user).order_by('id')
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

class ProjectHistoryEmployeeView(LoginRequiredMixin, ListView):
    template_name = 'project/listP.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historial de Proyectos'
        context['projects'] = Project.objects.filter(empleado=self.request.user, fechaFin__lt = datetime.now() )
    
    def get_queryset(self):
        return Project.objects.filter(empleado=self.request.user, fechaFin__lt = datetime.now() )

class ProjectHistoryClientView(LoginRequiredMixin, ListView):
    template_name = 'project/listP.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Historial de Proyectos'
        projects = Project.objects.filter(participa__cliente = self.request.user, fechaFin__lt = datetime.now())
        context['projects'] = projects
        return context

class ProjectNext(LoginRequiredMixin, ListView):
    template_name = 'project/listP.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Próximos Proyectos'
        projects = Project.objects.filter(fechaInicio__gte = (datetime.strftime((datetime.today() + timedelta(days=-datetime.today().weekday(), weeks=1)), '%Y-%m-%d')))
        context['projects'] = projects
        return context
        
        # print(datetime.strftime((datetime.today() + timedelta(days=-datetime.today().weekday(), weeks=1)), '%Y-%m-%d')) 

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
        elif fechaIni is None and fechaFin is None:
            projects = Project.objects.filter().exclude(pk__in = idProj)
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

@method_decorator(owns_project, name="dispatch")
class ProjectClientsView(LoginRequiredMixin, ListView):
    paginate_by = 5
    page_kwarg = 'page'
    status_kwarg = 'status'
    model = User
    ordering = ['pk']
    template_name = 'project/listPC.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cliente en este proyecto'       
        context['page_obj'] = Participa.objects.filter(proyecto_id=self.kwargs.get('pk'))       
        print(context['page_obj'])
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

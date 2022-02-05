from django.http import Http404
from django.http.response import HttpResponseRedirect
from core.project.models import Project
from core.user.models import User
from django.contrib import messages

def same_user(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(pk=pk)
        
        if not request.user.is_superuser:
            if not (user.id == request.user.id):
                messages.success(request, 'Acción no permitida')
                if request.user.role_user == 'Cliente':
                    return HttpResponseRedirect('/')
                elif request.user.role_user == 'Empleado':
                    return HttpResponseRedirect('/')

        return func(request, *args, **kwargs)

    return check_and_call

def is_admin(func):
    def check_and_call(request, *args, **kwargs):

        if request.user.is_superuser == 0:
            messages.success(request, 'Acción no permitida')
            return HttpResponseRedirect('/')

        return func(request, *args, **kwargs)

    return check_and_call

def is_client(func):
    def check_and_call(request, *args, **kwargs):

        if not (request.user.role_user == 'Cliente'):
            messages.success(request, 'Acción no permitida')
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)

    return check_and_call

def is_employee(func):
    def check_and_call(request, *args, **kwargs):

        if not (request.user.role_user == 'Empleado'):
            messages.success(request, 'Acción no permitida')
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)

    return check_and_call

def client_project(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs['pk']
        
        project_owner = Project.objects.get(pk=pk).empleado
        
        if not request.user.role_user == 'Cliente':
            if not (project_owner == request.user):
                messages.success(request, 'Acción no permitida')
                if request.user.role_user == 'Cliente':
                    return HttpResponseRedirect('/')
            
        return func(request, *args, **kwargs)

    return check_and_call

def employee_project(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs['pk']
        
        project_owner = Project.objects.get(pk=pk).empleado
        
        if not request.user.role_user == 'Cliente':
            if not (project_owner == request.user):
                messages.success(request, 'Acción no permitida')
                if request.user.role_user == 'Cliente':
                    return HttpResponseRedirect('/')
            
        return func(request, *args, **kwargs)

    return check_and_call

def owns_project(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            project_owner = Project.objects.get(pk=pk).empleado
        except Project.DoesNotExist:
            messages.success(request, 'Acción no permitida')
            return HttpResponseRedirect('/')
        
        if not request.user.is_superuser:
            if not (project_owner == request.user):
                messages.success(request, 'Acción no permitida')
                if request.user.role_user == 'Cliente':
                    return HttpResponseRedirect('/')
                elif request.user.role_user == 'Empleado':
                    return HttpResponseRedirect('/')

        return func(request, *args, **kwargs)

    return check_and_call

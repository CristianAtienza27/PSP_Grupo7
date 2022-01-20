from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from core.client.forms import ClientForm
from core.category.forms import CategoryForm
from core.user.models import User
from core.category.models import Category
from core.employee.models import Employee
from core.employee.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ValidatePermissionRequiredMixin

# Create your views here.
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    # permission_required = '.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['categories'] = Category.objects.all()
        context['create_url'] = reverse_lazy('adm:category_create')
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    # permission_required = '.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categoría'
        context['create_url'] = reverse_lazy('adm:category_list')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'Categoría registrada con éxito')
            url = reverse('adm:category_list')
            return HttpResponseRedirect(url)        
        else:
            return self.render_to_response(self.get_context_data(form=form))

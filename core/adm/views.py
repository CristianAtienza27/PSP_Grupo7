from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
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

    

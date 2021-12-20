from django.shortcuts import render
from nucleo.models import User
from nucleo.forms import UserCreate
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'home/index.html')

class ClientCreateView(CreateView):
    model = User
    form_class = UserCreate
    success_url = '/'
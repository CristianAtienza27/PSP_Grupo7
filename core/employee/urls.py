from django.urls import path
from core.employee.views import *

app_name = 'employee'

urlpatterns = [
    path('add/', EmployeeCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='client_update'),
]
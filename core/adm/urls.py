from django.urls import path
from core.client.views import *
from core.employee.views import *
from core.category.views import *

app_name = 'adm'

urlpatterns = [
    #Clientes
    path('/client/list/', ClientListView.as_view(), name='client_list'),
    path('/client/activate/<int:pk>/', ClientActivateView, name='client_activate'),
    path('/client/deactivate/<int:pk>/', ClientDeactivateView, name='client_deactivate'),
    path('/client/add/', ClientCreateView.as_view(), name='client_create'),
    path('/client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('/client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    #Empleados
    path('/employees/list/', EmployeeListView.as_view(), name='employee_list'),
    path('/employee/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('/employee/update/<int:pk>/', ClientUpdateView.as_view(), name='employee_update'),
    path('/employee/delete/<int:pk>/', ClientDeleteView.as_view(), name='employee_delete'),

    #Categorías
    path('/categories/list/', CategoryListView.as_view(), name='category_list'),
    path('/category/create/', CategoryCreateView.as_view(), name='category_create')
]
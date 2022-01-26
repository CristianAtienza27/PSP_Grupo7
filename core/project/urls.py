from core.project.views import *
from django.urls import path

app_name = 'project'

urlpatterns = [
    path('project/list/', ProjectListView.as_view(), name='project_list'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
]
    #Categorías
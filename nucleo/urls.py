from django.urls import path
from nucleo import views

urlpatterns = [
    path('createClient', views.ClientCreateView.as_view(), name="createClient")
]
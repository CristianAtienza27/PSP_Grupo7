from core.Api.views import *
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('login', LoginView.as_view())
]
from django.contrib import admin

# Register your models here.
from core.user.models import User
# from core.client.models import Client

admin.site.register(User)
# admin.site.register(Client)

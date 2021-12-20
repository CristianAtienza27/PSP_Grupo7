from django.contrib import admin
from django.contrib.auth.models import Permission
from nucleo.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Specialities: ',
            {
                'fields': (
                    'dni',
                    'direccion',
                    'fechaNacimiento',
                    'fechaAlta',
                    'biografia',
                    'is_client',
                    'activo',
                ),
            },
        ),
    )
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_client', 'activo')
    list_filter = ['is_client', 'activo']


admin.site.register(User, UserAdmin)
admin.site.register(Permission)

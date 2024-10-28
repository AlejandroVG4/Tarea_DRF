from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Usuarios
    list_display = ['email', 'username', 'pais', 'is_staff', 'direccion']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('direccion', 'pais', 'telefono')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('direccion', 'pais', 'telefono')}),)
    
admin.site.register(Usuarios, CustomUserAdmin)
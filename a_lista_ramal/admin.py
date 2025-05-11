from django.contrib import admin
from .models import *

@admin.register(Ramal)
class RamalAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'nome_completo', 'email', 'ramal','anydesk') 
    search_fields = ('nome_usuario', 'nome_completo', 'email', 'ramal','anydesk')  
    ordering = ('nome_usuario',) 
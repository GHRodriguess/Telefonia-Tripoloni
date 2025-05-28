from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Linha)
class LinhasAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'nome_completo', 'numero', 'pacote_formatado', 'setor', 'obra', 'imprimir')
    search_fields = ('nome_usuario', 'nome_completo', 'numero', 'setor', 'obra')    
    ordering = ('nome_usuario',)
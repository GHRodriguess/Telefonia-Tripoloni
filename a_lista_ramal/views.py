from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *
from .utils import *

@check_permission(permissions=['login_required'])
def lista_ramal(request, busca=None,filtro=None):
    context = {}
    #busca
    busca, ramais = filtro_busca(request)
    #obra
    ramais = filtro_obra(request, ramais)

    ramais = ramais.order_by('obra', 'setor')   
    context["ramais"] = ramais
    context["busca"] = busca 
    return render(request, "lista_ramal.html", context=context)


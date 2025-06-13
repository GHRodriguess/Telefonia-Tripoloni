from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *
from .utils import *

def lista_ramal(request,busca=None, filtro=None, order_by=None):
    context = {}
    #busca
    busca, ramais = filtro_busca(request)
    #obra
    ramais = filtro_obra(request, ramais)
    #order_by 
    ramais = ramais_order(request, ramais)   

    context["ramais"] = ramais
    context["busca"] = busca 
    return render(request, "lista_ramal.html", context=context)


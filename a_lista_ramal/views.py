from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *
from .utils import *

@check_permission(permissions=['login_required'])
def lista_ramal(request, filtro=None):
    context = {}
    busca = request.GET.get("busca", None)
    filtro = request.GET.get("filtro", None)
    if busca:
        ramais = filter_ramal(busca)
    else:
        ramais = Ramal.objects.all()
    if filtro:        
        ramais = filter_ramal_obra(filtro)        
    ramais = ramais.order_by('obra', 'setor')   
    context["ramais"] = ramais
    return render(request, "lista_ramal.html", context=context)
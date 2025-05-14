from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *
from .utils import *

@check_permission(permissions=['login_required'])
def lista_ramal(request):
    context = {}
    busca = request.GET.get("busca", None)
    if busca:
        ramais = filter_ramal(busca)
    else:
        ramais = Ramal.objects.all()
    ramais = ramais.order_by('setor')
    context["ramais"] = ramais
    return render(request, "lista_ramal.html", context=context)
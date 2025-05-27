from django.db.models import Q
from .models import *

def filtro_busca(request):
    busca_get = request.GET.get("busca")
    if busca_get is not None:
        request.session["busca"] = busca_get        
    busca = request.session["busca"]
    if busca:
        ramais = filter_ramal(busca)
    else:
        ramais = Ramal.objects.all()
    return busca, ramais

def filtro_obra(request, ramais):
    filtro = request.GET.get("filtro", None) 
    if filtro:                
        request.session["filtro"] = request.session.get("filtro", {"central": False, "obra": False})
        request.session["filtro"][filtro] = False if request.session["filtro"][filtro] else True
    filtros = request.session["filtro"]
    for filtro, status in filtros.items():        
        if status:
            ramais = filter_ramal_obra(filtro, ramais)
    return ramais
#filtros
def filter_ramal(termo):
    return Ramal.objects.filter(
    Q(nome_usuario__icontains=termo) |
    Q(nome_completo__icontains=termo) |
    Q(email__icontains=termo) |
    Q(setor__icontains=termo) |
    Q(nome__icontains=termo) |
    Q(sobrenome__icontains=termo) |
    Q(ramal__icontains=termo) |
    Q(anydesk__icontains=termo)
)

def filter_ramal_obra(termo, ramais):
    return ramais.filter(
    Q(obra__icontains=termo) 
)
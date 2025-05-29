from django.db.models import Q, F, Case, When, Value, IntegerField, OrderBy
from .models import *

def filtro_busca(request):
    busca_get = request.GET.get("busca")
    if busca_get is not None:
        request.session["busca"] = busca_get    
    try:    
        busca = request.session["busca"]
    except:
        request.session["busca"] = "" 
        busca = request.session["busca"]
        
    if busca:
        ramais = filter_ramal(busca)
    else:
        ramais = Ramal.objects.all()
    return busca, ramais

def filtro_obra(request, ramais):
    filtro = request.GET.get("filtro", None) 
    request.session["filtro"] = request.session.get("filtro", {"central": False, "obra": False})
    if filtro:   
        request.session["filtro"][filtro] = False if request.session["filtro"][filtro] else True
    filtros = request.session["filtro"]
    for filtro, status in filtros.items():        
        if status:
            ramais = filter_ramal_obra(filtro, ramais)
    return ramais

def ramais_order(request, ramais):
    order_by = request.GET.get("order_by")  
    if order_by:
        request.session["order_by"] = order_by
    else:
        order_by = request.session.get("order_by", None)        
        request.session["order_by"] = order_by
        request.session.modified = True 
    order_by = request.session["order_by"] 
    if order_by:
        ramais = ramais.annotate(
            vazio_primeiro=Case(
                When(**{f"{order_by}": ""}, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('vazio_primeiro', OrderBy(F(order_by), nulls_last=True))
    else:
        ramais = ramais.order_by('obra', 'setor')
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
    Q(anydesk__icontains=termo) |
    Q(obra__icontains=termo) 
)

def filter_ramal_obra(termo, ramais):
    return ramais.filter(
    Q(obra__icontains=termo) 
)
from django.db.models import Q
from .models import *

def filter_ramal(termo):
    return Ramal.objects.filter(
    Q(nome_usuario__icontains=termo) |
    Q(nome_completo__icontains=termo) |
    Q(email__icontains=termo) |
    Q(nome__icontains=termo) |
    Q(sobrenome__icontains=termo) |
    Q(ramal__icontains=termo) |
    Q(anydesk__icontains=termo)
)

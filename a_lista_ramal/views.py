from django.shortcuts import render
from utils.global_utils import  check_permission


@check_permission(permissions=['login_required'])
def lista_ramal(request):
    return render(request, "lista_ramal.html")
from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *

@check_permission(permissions=['login_required'])
def lista_ramal(request):
    context = {}
    ramais = Ramal.objects.all()
    context["ramais"] = ramais
    return render(request, "lista_ramal.html", context=context)
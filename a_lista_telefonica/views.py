from django.shortcuts import render
from utils.global_utils import  check_permission
from .models import *


@check_permission(permissions=['login_required', "ti_member"])
def lista_telefonica(request):
    context = {}
    
    return render(request, "lista_telefonica.html", context=context)
from django.shortcuts import render
from utils.global_utils import  check_permission
from .utils import *

@check_permission(permissions=['login_required'])
def home(request):  
    limpar_sessao(request)
    return render(request, "home.html")
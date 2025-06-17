from django.shortcuts import render
from utils.global_utils import  check_permission
from .utils import *

def home(request):  
    limpar_sessao(request)
    context = {}
    context['apps'] = apps(request)
    return render(request, "home.html", context=context)
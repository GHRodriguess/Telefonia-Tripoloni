from django.shortcuts import render
from utils.global_utils import  check_permission
from .utils import *

def home(request):  
    limpar_sessao(request)
    deletar_errados()
    return render(request, "home.html")
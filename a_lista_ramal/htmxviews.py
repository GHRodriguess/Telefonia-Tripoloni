from django.shortcuts import render
from .models import *

def add_ramal(request, open_status, ramal_id=None):
    context = {}    
    if ramal_id:
        context["id"] = ramal_id
        ramal = Ramal.objects.filter(id=ramal_id).first()
        print(ramal.nome_usuario)
        print(ramal.nome_completo)
        print(ramal.email)
        print(ramal.nome)
        print(ramal.sobrenome)
        print(ramal.ramal) 
        print(ramal.anydesk)
    context["open"] = "open" if open_status== "True" else ""
    if request.method == "POST":
        print("post")
    return render(request, "partials/add_ramal.html", context=context) 
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else "" 
    if request.method == "POST":
        print("POST")
    return render(request, "partials/edit_ramal.html", context=context) 

def edit_ramal(request, open_status, ramal_id):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""  
    if ramal_id:
        ramal = get_object_or_404(Ramal, id=ramal_id)
        print(ramal)
        context["id"] = ramal_id
        ramal = Ramal.objects.filter(id=ramal_id).first()
        print(ramal.nome_usuario)
        print(ramal.nome_completo)
        print(ramal.email)
        print(ramal.nome)
        print(ramal.sobrenome)
        print(ramal.ramal) 
        print(ramal.anydesk)
        
    return render(request, "partials/edit_ramal.html", context=context) 

def save_ramal(request, open_status, ramal_id=None):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""  
    if ramal_id:
        print("Tem ramal id, dar UPDATE")
    else:
        print("Não tem ramal ID, CRIAR")
    
    return redirect('lista_ramal')

def cancel_add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else "" 
    return render(request, "partials/edit_ramal.html", context=context) 

def delete_ramal(request, open_status, ramal_id):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""    
    if ramal_id:
        ramal = get_object_or_404(Ramal, id=ramal_id)
        print(ramal)
        ramal.delete()
    return redirect('lista_ramal')
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import *
from utils.conection_ad import *
from .utils import *

def add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else ""     
    return render(request, "partials/edit_ramal.html", context=context) 

def edit_ramal(request, open_status, ramal_id):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""  
    if ramal_id:
        ramal = get_object_or_404(Ramal, id=ramal_id)
        context["id"] = ramal_id
        ramal = Ramal.objects.filter(id=ramal_id).first()
        context["nome_usuario"] = ramal.nome_usuario
        context["nome_completo"] = f"{ramal.nome} {ramal.sobrenome}" 
        context["email"] = ramal.email
        context["nome"] = ramal.nome
        context["sobrenome"] = ramal.sobrenome
        context["ramal"] = ramal.ramal
        context["anydesk"] = ramal.anydesk
        context["setor"] = ramal.setor  
        
    return render(request, "partials/edit_ramal.html", context=context) 

def save_ramal(request, open_status, ramal_id=None):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""  
    if request.method == "POST":
        nome_usuario = request.POST.get("nome_usuario")
        nome_completo = request.POST.get("nome_completo")
        email = request.POST.get("email")
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        ramal = request.POST.get("ramal")
        anydesk = request.POST.get("anydesk")
        setor = request.POST.get("setor")
    
        ramal, criado = Ramal.objects.update_or_create(
        nome_usuario=nome_usuario,
        defaults={
            'nome_completo': nome_completo,
            'email': email,
            'nome': nome,
            'sobrenome': sobrenome,
            'ramal': ramal,
            'anydesk': anydesk,
            'setor': setor
        })   
    
    return redirect("lista_ramal")

def cancel_add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else "" 
    return render(request, "partials/edit_ramal.html", context=context) 

def delete_ramal(request, open_status, ramal_id):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""    
    if ramal_id:
        ramal = get_object_or_404(Ramal, id=ramal_id)        
        ramal.delete()
        
    return redirect("lista_ramal")

def get_data_ad(request):
    context = {}
    context["open"] = "open"    
    if request.method == "POST":        
        conexao_ad = Conexão_AD()
        nome_usuario = request.POST.get("nome_usuario")
        context["nome_usuario"] = nome_usuario 
        data = conexao_ad.get_info_user(nome_usuario)  
        if data:              
            context["nome_usuario"] = nome_usuario 
            context["nome_completo"] = f"{data.get('nome', '')} {data.get('sobrenome', '')}" 
            context["email"] = data.get("email", "")
            context["nome"] = data.get("nome", "")
            context["sobrenome"] = data.get("sobrenome", "")     
            context["setor"] = data.get("setor", "")    
        
    return render(request, "partials/edit_ramal.html", context=context) 


def gerar_pdf(request):  
    ramais = Ramal.objects.all()
    ramais = ramais.order_by("setor")
    html_string = render_to_string('partials/tabela_ramal_pdf.html', {'ramais': ramais, 'request': request})
    pdf_bytes = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()

    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ramais.pdf"'  # força download
    return response
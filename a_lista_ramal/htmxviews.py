from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse
from weasyprint import HTML
from utils.global_utils import  check_permission
from .models import *
from utils.conection_ad import *
from .utils import *

@check_permission(permissions=['login_required', 'ti_member'])
def add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else ""     
    return render(request, "partials/edit_ramal.html", context=context) 

@check_permission(permissions=['login_required', 'ti_member'])
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
        context["numero_celular"] = ramal.numero_celular
        context["anydesk"] = ramal.anydesk
        context["setor"] = ramal.setor
        context["obra"] = ramal.obra  
        
    return render(request, "partials/edit_ramal.html", context=context) 

@check_permission(permissions=['login_required', 'ti_member'])
def save_ramal(request, open_status, ramal_id=None):
    context = {}        
    context["open"] = "open" if open_status== "True" else ""  
    if request.method == "POST":
        nome_usuario = request.POST.get("nome_usuario", None)
        nome_completo = request.POST.get("nome_completo")
        email = request.POST.get("email")        
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        ramal = request.POST.get("ramal")
        numero_celular = request.POST.get("numero_celular")
        
        anydesk = request.POST.get("anydesk")
        setor = request.POST.get("setor")
        obra = request.POST.get("obra")        
        if nome_usuario == "":
            ramal, criado = Ramal.objects.update_or_create(
            nome_completo=nome_completo,
            defaults={
                'nome_usuario': nome_usuario or '',
                'email': email or '',
                'nome': nome or '',
                'sobrenome': sobrenome or '',
                'ramal': ramal or '',
                'numero_celular': numero_celular or '',
                'anydesk': anydesk or '',
                'setor': setor or '',
                'obra': obra or ''
            })   
        else:
            ramal, criado = Ramal.objects.update_or_create(
            nome_usuario=nome_usuario,
            defaults={
                'nome_completo': nome_completo or '',
                'email': email or '',
                'nome': nome or '',
                'sobrenome': sobrenome or '',
                'ramal': ramal or '',
                'numero_celular': numero_celular or '',
                'anydesk': anydesk or '',
                'setor': setor or '',
                'obra': obra or ''
            })  
    return redirect("lista_ramal")

@check_permission(permissions=['login_required', 'ti_member'])
def cancel_add_ramal(request, open_status):
    context = {}   
    context["open"] = "open" if open_status== "True" else "" 
    return render(request, "partials/edit_ramal.html", context=context) 

@check_permission(permissions=['login_required', 'ti_member'])
def delete_ramal(request, open_status, ramal_id):
    context = {}    
    context["open"] = "open" if open_status== "True" else ""    
    if ramal_id:
        ramal = get_object_or_404(Ramal, id=ramal_id)        
        ramal.delete()
        
    return redirect("lista_ramal")

def filtra_central(request):
    filtro = request.GET.get("filtro", None)
    print(filtro)
    url = reverse("lista_ramal") + f"?filtro={filtro}"    
    print(url)
    return redirect(url)

@check_permission(permissions=['login_required', 'ti_member'])
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
            context["nome_completo"] = f"{data.get('nome') or ''} {data.get('sobrenome') or ''}"
            context["email"] = data.get("email", "")
            context["nome"] = data.get("nome", "")
            context["sobrenome"] = data.get("sobrenome", "")     
            context["setor"] = data.get("setor", "")  
            context["obra"] = data.get("obra", "") 
            try:
                r_usuario = Ramal.objects.filter(nome_usuario=nome_usuario).first()
                if r_usuario:
                    context["ramal"] = r_usuario.ramal
                    context["anydesk"] = r_usuario.anydesk
            except:
                pass
        
    return render(request, "partials/edit_ramal.html", context=context)

def gerar_pdf(request):      
    ramais = Ramal.objects.all()    
    ramais = ramais.order_by("obra", "setor")
    html_string = render_to_string('partials/tabela_ramal_pdf.html', {'ramais': ramais, 'request': request})
    pdf_bytes = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ramais.pdf"'
    return response

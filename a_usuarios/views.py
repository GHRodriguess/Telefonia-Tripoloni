from django.shortcuts import render, redirect
from utils.global_utils import  check_permission
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from .utils import *

User = get_user_model()

# Create your views here.
def login_view(request):     
    context = {}   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        conexao_ad = Conexão_AD(username, password)
        autenticated = conexao_ad.autenticar_usuario_ad() 
        if autenticated:            
            info_user = conexao_ad.get_info_user() 
            grupos = info_user.get("grupos", [])
            adm = True if any(grupo.split(",")[0].replace("CN=", "") == "ti" for grupo in grupos) else False 
            user, created = User.objects.get_or_create(email=info_user.get("email", ""), defaults={
                "username": username,
                "first_name": info_user.get("nome", ""),
                "last_name": info_user.get("sobrenome", ""),
                "is_staff": adm,
                "is_superuser": adm
            })   
            if not created: 
                user.first_name = info_user.get("nome", "")
                user.last_name = info_user.get("sobrenome", "")
                user.is_staff = adm
                user.is_superuser = adm
                user.groups.clear()                
                
            for grupo in grupos:
                grupo_nome = grupo.split(",")[0].replace("CN=", "")    
                grupo_obj, _ = Group.objects.get_or_create(name=grupo_nome)                
                user.groups.add(grupo_obj) 
                
            user.save()
            login(request, user)            
            return redirect("home")
        
        else:
            context["message"] = "Nome de usuário ou senha incorretos"
            
    return render(request, "login.html", context=context)

@check_permission(permissions=['login_required'])
def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from utils.global_utils import  check_permission
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login_view(request):    
    return render(request, "login.html")

@check_permission(permissions=['login_required'])
def logout_view(request):
    logout(request)
    return redirect('hub')
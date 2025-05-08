from django.shortcuts import render
from utils.global_utils import  check_permission

@check_permission(permissions=['login_required'])
def home(request):
    return render(request, "home.html")
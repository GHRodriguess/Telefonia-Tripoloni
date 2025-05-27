from django.shortcuts import render

# Create your views here.
def lista_telefonica(request):
    context = {}
    return render(request, "lista_telefonica.html", context=context)
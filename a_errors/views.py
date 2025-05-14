from django.shortcuts import render

# Create your views here.
def page_401(request):
    return render(request, "401.html", status=401)

def page_404(request, exception):
    return render(request, "404.html", status=404)
"""
URL configuration for p_telefonia_tripoloni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

handler404 = 'a_errors.views.page_404'
handler401 = 'a_errors.views.page_401'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("a_usuarios.urls")),
    path('', include("a_home.urls")), 
    path('ramal/', include("a_lista_ramal.urls")),
    path('', include("a_errors.urls")), 
] 
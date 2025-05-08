from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_ramal, name="lista_ramal"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("401", views.page_401, name="page_401"),
    path("404", views.page_404, name="page_404"),
]

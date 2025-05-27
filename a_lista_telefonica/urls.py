from django.urls import path
from . import views
from . import htmxviews

urlpatterns = [
    path('', views.lista_telefonica, name="lista_telefonica"),
] 

htmxurlpatterns = [ 

]
urlpatterns += htmxurlpatterns
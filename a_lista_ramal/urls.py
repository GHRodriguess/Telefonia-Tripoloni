from django.urls import path, re_path
from . import views
from . import htmxviews

urlpatterns = [
    path("", views.lista_ramal, name="lista_ramal"),
]

htmxurlpatterns = [
    re_path(r"^add_ramal/(?P<open_status>\w+)/(?:/(?P<ramal_id>\w+))?$", htmxviews.add_ramal, name="add_ramal"),
]

urlpatterns += htmxurlpatterns

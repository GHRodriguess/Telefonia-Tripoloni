from django.urls import path, re_path
from . import views
from . import htmxviews

urlpatterns = [
    path("", views.lista_ramal, name="lista_ramal"),
]

htmxurlpatterns = [
    path("add_ramal/<str:open_status>", htmxviews.add_ramal, name="add_ramal"),
    path("edit_ramal/<str:open_status>/<int:ramal_id>", htmxviews.edit_ramal, name="edit_ramal"),
    re_path(r"^save_ramal/(?P<open_status>\w+)/(?:/(?P<ramal_id>\d+))?$", htmxviews.save_ramal, name="save_ramal"),
    path("cancel_add_ramal/<str:open_status>", htmxviews.cancel_add_ramal, name="cancel_add_ramal"),
    path("delete_ramal/<str:open_status>/<int:ramal_id>", htmxviews.delete_ramal, name="delete_ramal"),
    path("filtra_central", htmxviews.filtra_central, name="filtra_central"),
    #funções sem retorno de html
    path("get_data_ad", htmxviews.get_data_ad, name="get_data_ad"),
    path("gerar_pdf", htmxviews.gerar_pdf, name="gerar_pdf"),
    path("conecta_anydesk/<str:anydesk_id>", htmxviews.conecta_anydesk, name="conecta_anydesk"),
]

urlpatterns += htmxurlpatterns

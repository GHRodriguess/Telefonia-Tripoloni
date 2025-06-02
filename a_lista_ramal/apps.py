from django.apps import AppConfig


class AListaRamalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_lista_ramal'

    def ready(self):
        from .tasks import iniciar_verificacao_periodica
        iniciar_verificacao_periodica()
from django.apps import AppConfig


class AListaRamalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_lista_ramal'

    def ready(self):
        from .tasks import lista_ramal_tasks
        lista_ramal_tasks()        
        
from django.apps import AppConfig
import sys
from django.core.management import call_command

class AHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_home'

    def ready(self):        
        if 'runserver.py' in sys.argv:
            try:
                call_command('collectstatic', interactive=False, verbosity=0)
                print("✅ Arquivos estáticos coletados automaticamente.")
            except Exception as e:
                print("❌ Erro ao rodar collectstatic automaticamente:", e)

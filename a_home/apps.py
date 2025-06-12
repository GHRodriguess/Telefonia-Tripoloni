from django.apps import AppConfig
import sys
import subprocess
from django.core.management import call_command

class AHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_home'

    def ready(self):        
        if 'runserver.py' in sys.argv:
            try:
                call_command('collectstatic', interactive=False, verbosity=0)
                print("✅ Arquivos estáticos coletados automaticamente.")
                subprocess.run(['git', 'add', 'staticfiles/'], check=True)
                subprocess.run(['git', 'commit', '-m', 'Atualizando os arquivos estáticos após collectstatic (automático)'])
                subprocess.run(['git', 'push'], check=True)
                print("✅ Commit automático feito com sucesso.")
            except subprocess.CalledProcessError as e:
                print("❌ Erro ao executar comando Git:", e)
            except Exception as e:
                print("❌ Erro ao rodar collectstatic automaticamente:", e)

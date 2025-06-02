import threading
import time
import pandas as pd
from .models import *
from utils.conection_ad import *

def listar_usuarios():    
    conexao_ad = Conexão_AD()  
    usuarios = conexao_ad.get_all_users('active')

def adicionar_todos_usuarios():
    conexao_ad = Conexão_AD()
    df = pd.read_excel("usuarios_ad.xlsx")
    usuarios = df['sAMAccountName'].tolist()
    for usuario in usuarios:
        user_data = conexao_ad.get_info_user(usuario)
        
        if not Ramal.objects.filter(nome_usuario=usuario).exists():
            ramal = Ramal(
                nome_completo=user_data.get("nome") or "" + user_data.get("sobrenome") or "",  
                email=user_data.get("email") or "",
                nome=user_data.get("nome") or "",
                sobrenome=user_data.get("sobrenome") or "",
                setor=user_data.get("setor") or "",
                obra=user_data.get("obra") or "",
                nome_usuario=usuario
            )
            ramal.save()

def verificar_inativos():
    conexao_ad = Conexão_AD()
    usuarios = conexao_ad.get_all_users('inactive')
    for usuario in usuarios:
        try:
            ramal = Ramal.objects.get(nome_usuario=usuario)
            ramal.delete()
            print(f"Ramal {usuario} deletado com sucesso.")
        except Ramal.DoesNotExist:
            continue
    print("finalizado a verificao de inativos.")
        
def iniciar_verificacao_periodica():
    def tarefa():
        while True:
            verificar_inativos()
            time.sleep(60) 

    thread = threading.Thread(target=tarefa, daemon=True)
    thread.start()
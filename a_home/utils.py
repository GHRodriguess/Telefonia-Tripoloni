from utils.conection_ad import *
import pandas as pd
from django.db.models import Q
from a_lista_ramal.models import Ramal
import sqlite3

def limpar_sessao(request):
    #caso queira manter outro item coloque nessa lista
    important_keys = ['next', '_auth_user_id', '_auth_user_backend', '_auth_user_hash', 'order_by']
    keys_to_remove = [k for k in request.session.keys() if k not in important_keys]
    for k in keys_to_remove:
        del request.session[k]
    request.session.midified = True
    

def exportando_dados():
    conn = sqlite3.connect('db copy.sqlite3')
    tabelas = ['a_lista_ramal_ramal', 'a_lista_telefonica_linha', "auth_group", "auth_group_permissions", "auth_user", "auth_permission", "auth_user_groups", "auth_user_user_permissions", "django_admin_log", "django_content_type", "django_migrations", "django_session", "sqlite_sequence"]
    for tabela in tabelas:
        
        print(tabela) 
        
        df = pd.read_sql_query(f"SELECT * FROM {tabela}", conn)

        #df.to_csv(f'tabelas/{tabela}.csv', index=False)
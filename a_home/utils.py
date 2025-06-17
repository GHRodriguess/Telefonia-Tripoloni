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
    
def apps(request):
    #parar criar mais apps na tela inicial adicione aqui
    
    #chaves opcionais ['filtro']
    
    apps = {
        "LISTA RAMAL": { 
            'name_app': 'LISTA DE RAMAL',
            'url': 'filtra_central',
            'filtro': 'central',
            'img': 'a_home/src/ramal.svg',
            "permissions": True
        },
        "LISTA TELEFONES OBRA": {
            'name_app': 'LISTA DE TELEFONES OBRA',
            'url': 'filtra_central',
            'filtro': 'obra',
            'img': 'a_home/src/ramal.svg',
            "permissions": True
        },
    #    "GERENCIAMENTO DE CHIPS": {
    #        "name_app": "GERENCIAMENTO DE CHIPS",
    #        "url": "lista_telefonica",
    #        "img": "a_home/src/phone.svg",   
    #        "permissions": request.user.is_staff

    #   }
    }
    return apps
    
# FUNÇÕES CRIADAS APENAS PARA TRANSFERIR O BANCO DE DADOS
def exportando_dados():
    conn = sqlite3.connect('db.sqlite3')
    tabelas = ['a_lista_ramal_ramal']
    for tabela in tabelas:       
          
        df = pd.read_sql_query(f"SELECT * FROM {tabela}", conn)
        df.to_excel(f'tabelas/{tabela}.xlsx', index=False)
        
def importando_dados():
    df = pd.read_excel('tabelas/a_lista_ramal_ramal.xlsx')
    for _, row in df.iterrows():
        ramal_raw = row['ramal']
        anydesk_raw = row['anydesk']
        campos_nulos = ['email', 'nome_usuario', 'nome_completo', 'nome', 'sobrenome', 'setor', 'obra']
        if pd.isna(ramal_raw):
            ramal = ''
        else:
            ramal = str(int(float(ramal_raw))).strip()[:4]
            
        if pd.isna(anydesk_raw):
            anydesk = ''
        else:
            anydesk = str(int(float(anydesk_raw))).strip()[:10]
            
        for campo_nulo in campos_nulos:
            if pd.isna(row[campo_nulo]):
                row[campo_nulo] = ''
            
        Ramal.objects.update_or_create(
            id=row['id'],
            defaults={
                'nome_usuario': row.get('nome_usuario', '') or '',
                'nome_completo': row.get('nome_completo', '') or '',
                'email': row.get('email', '') or '',
                'nome': row.get('nome', '') or '',
                'sobrenome': row.get('sobrenome', '') or '',
                'anydesk': anydesk,
                'ramal': ramal,
                'setor': row.get('setor', '') or '',
                'obra': row.get('obra', '') or '',
            }
        )
        
def limpando_dados(): 
    Ramal.objects.all().delete()

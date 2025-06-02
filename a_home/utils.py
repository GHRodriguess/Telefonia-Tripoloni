from utils.conection_ad import *
import pandas as pd
from django.db.models import Q
from a_lista_ramal.models import Ramal

def limpar_sessao(request):
    #caso queira manter outro item coloque nessa lista
    important_keys = ['next', '_auth_user_id', '_auth_user_backend', '_auth_user_hash', 'order_by']
    keys_to_remove = [k for k in request.session.keys() if k not in important_keys]
    for k in keys_to_remove:
        del request.session[k]
    request.session.midified = True
    

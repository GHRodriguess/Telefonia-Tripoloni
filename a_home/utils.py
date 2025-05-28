def limpar_sessao(request):
    #caso queira manter outro item coloque nessa lista
    important_keys = ['next', '_auth_user_id', '_auth_user_backend', '_auth_user_hash']
    keys_to_remove = [k for k in request.session.keys() if k not in important_keys]
    for k in keys_to_remove:
        del request.session[k]
    request.session.midified = True
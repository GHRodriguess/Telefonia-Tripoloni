def check_permission(permissions=[]):
    from functools import wraps
    from django.shortcuts import redirect
    from django.urls import reverse
    from .permissions import Permissions
    
    actions = {
        'redirect': redirect,
    }
    
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **view_kwargs):
            permission = Permissions(request, request.user, permissions, **view_kwargs)
            retorno = permission.check_permissions() 
            
            for perm in retorno:
                perm_name = perm[0]
                has_perm = perm[1]
                if not has_perm:
                    action, *args = permission.all_permissions.get(perm_name,None).get('action', None)
                    has_next_url = permission.all_permissions.get(perm_name, None).get('next', None)
                    if has_next_url:
                        current_url = request.get_full_path()                    
                        redirect_url = reverse(*args)                    
                        url = f"{redirect_url}?next={current_url}"                    
                        request.session['next'] = current_url                        
                    else:                        
                        url = reverse(*args)
                    return actions[action](url)
                
            return view_func(request, *args, **view_kwargs)  
        return _wrapped_view
    return decorator
"""
Para utilizar o permissions basta usar isso no inicio do código:
from utils.global_utils import  check_permission

E antes de cada view ou função utilizar o decorator abaixo:
@check_permission(permissions=[{permissoes_requeridas}])
"""


class Permissions: 
    def __init__(self, request, user, permissions=[], **kwargs):
        self.request = request
        self.user = user
        self.permissions = permissions
        self.kwargs = kwargs
        self.all_permissions = {
            'login_required': {
                'func': self.login_required,
                'message': 'You must be logged in',
                'action': ['redirect', 'login'],
                'next': True,
            },
        }
        
    def login_required(self):
        return self.user.is_authenticated   
    
    def check_permissions(self):
        user_permissions = []
        
        for str_permission in self.permissions:
            permission = self.all_permissions.get(str_permission, None)
            if permission is not None:
                permission = permission.get('func', None)
                try:
                    user_permission = [str_permission, permission()]
                    user_permissions.append(user_permission)
                except Exception as e:
                    user_permission = [str_permission, False]
                    user_permissions.append(user_permission)
            else:
                print("Permission not found")
                
        return user_permissions
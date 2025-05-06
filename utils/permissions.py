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
#            'in_course_required': {
#                'func': self.in_course_required,
#                'message': 'You must be a student or an instructor to access this course',
#                'action': ['redirect', 'hub'],
#                'next': False,
#            },
#            'is_teacher_required': {
#                'func': self.is_teacher_required,
#                'message': 'You must be a teacher to access this course',
#                'action': ['redirect', 'hub'],
#                'next': False,
#            }
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
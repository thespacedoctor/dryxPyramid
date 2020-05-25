from builtins import object
from pyramid.security import Allow, Everyone

class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view_everyone'),
               (Allow, 'group:view_users', ('view_everyone', 'view_users')),
               (Allow, 'group:edit_users',
                ('edit_users', 'view_everyone', 'view_users')),
               (Allow, 'group:superuser',
                ('view_everyone', 'view_users', 'edit_users', 'superuser')),
               (Allow, 'group:admin', ('view_everyone', 'view_users',
                                       'edit_users', 'superuser', 'admin')),
               (Allow, 'group:superadmin', ('view_everyone', 'view_users', 'edit_users', 'superuser', 'admin', 'superadmin'))]

    def __init__(self, request):
        pass

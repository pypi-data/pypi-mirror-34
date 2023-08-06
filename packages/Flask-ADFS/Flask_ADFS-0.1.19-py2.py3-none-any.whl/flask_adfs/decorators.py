from flask import current_app as app
from flask import abort
from flask_login import current_user
from flask_login import login_required
from functools import wraps
from .initialise import get_access

str = str
unicode = str
bytes = bytes
basestring = (str,bytes)


# decorater can be used with @role_required('viewer')
def role_required(permission):
    def _role_required(func):
        @login_required
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            # if the login is off!
            if app.config.get('LOGIN_DISABLED'):
                return func(*args, **kwargs)
            access = get_access()
            if 'channel' in kwargs:
                index = kwargs['channel']
            else:
                if 'index' in kwargs:
                    index = kwargs['index'] 
                else:
                    index = '_default' 
            if index not in access:
                abort(403, "Invalid Channel")
            permissions = []
            if isinstance(permission, basestring):
                permissions.append(permission)
            else:
                permissions = permission
            roles = []   
            for p in permissions: 
                roles.extend(access[index].get(p, set()))
            # if 'index' in kwargs:
            #     if kwargs['index'] not in access:
            #         abort(403, "Invalid Channel")
            #     roles = access[kwargs['index']].get(permission, set())
            # else:
            #     roles = access.get('_default', {}).get(permission, set())

            roles = set(roles)
            if roles.isdisjoint(current_user.get_roles()):
                abort(403, 'insufficent priviledge for this function' )

            return func(*args, **kwargs)
        return func_wrapper
    return _role_required

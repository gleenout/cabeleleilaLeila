from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Funcionario
'''
def is_staff_check(user):
    return user.is_staff'''

def is_admin(user):
    if hasattr(user, 'funcionario'):
        return user.funcionario.cargo == 'admin'
    return False

def staff_required(view_func):
    decorated_view = login_required(user_passes_test(is_admin, login_url='/acesso-negado/')(view_func))
    return decorated_view
'''
def staff_required(view_func):
    decorated_view = login_required(user_passes_test(is_staff_check, login_url='/acesso-negado/')(view_func))
    return decorated_view
'''
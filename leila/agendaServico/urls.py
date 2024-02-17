from django.urls import path
from .views import home, login, cadastro, servicos, agendamento, produtos

urlpatterns = [
    path('', home, name='home'),
    path('login/',login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('servicos/', servicos, name='servicos'),
    path('agendamento/', agendamento, name='agendamento'),
    path('produtos/', produtos, name='produtos'),
]


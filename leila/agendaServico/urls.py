from django.urls import path
from .views import home, servicos, agendamento, produtos, profile

urlpatterns = [
    path('', home, name='home'),
    path('servicos/', servicos, name='servicos'),
    path('agendamento/', agendamento, name='agendamento'),
    path('produtos/', produtos, name='produtos'),
    path('accounts/profile/', profile, name='profile'),
]


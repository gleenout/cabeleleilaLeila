from django.urls import path
from .views import home, servicos, agendamento, produtos

urlpatterns = [
    path('', home, name='home'),
    path('servicos/', servicos, name='servicos'),
    path('agendamento/', agendamento, name='agendamento'),
    path('produtos/', produtos, name='produtos'),
]


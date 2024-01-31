from django.urls import path
from .views import agendamento

urlpatterns =[
    path('', agendamento, name='agendamento')
]
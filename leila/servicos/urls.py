from django.urls import path
from .views import servicos

urlpatterns = [
    path('', servicos, name='servicos'),
]
from django.urls import path
from .views import home, servicos

urlpatterns = [
    path('', home, name='home'),
    path('servicos/', servicos, name='servicos'),
]
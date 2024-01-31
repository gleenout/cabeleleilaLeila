from django.urls import path
from .views import produtos

urlpatterns =[
    path('', produtos, name='produtos'),
]
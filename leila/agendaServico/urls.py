from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('produtos/', views.produtos, name='produtos'),
    path('login/',views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout, name='logout'),

    #Painel admnistrativo
    path('painel/', views.painel, name='painel'),
    path('painel/usuarios/', views.usuarios, name='usuarios'),
    path('painel/produtos/', views.tab_produtos, name='tab_produtos'),
    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

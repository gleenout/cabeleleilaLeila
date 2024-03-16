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
    path('dm/painel/', views.painel, name='painel'),
    path('dm/painel/usuarios/', views.tab_usuarios, name='usuarios'),
    path('dm/painel/produtos/', views.tab_produtos, name='tab_produtos'),
    path('dm/painel/servicos/', views.tab_servicos, name='tab_servicos'),
    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
    path('dm/painel/perfil/', views.admin_perfil, name='admin_perfil')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

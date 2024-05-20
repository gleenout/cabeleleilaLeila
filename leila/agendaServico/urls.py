from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from rest_framework import routers
from .viewset import FuncionarioViewSet

routers = routers.DefaultRouter()
routers.register(r'funcionario', FuncionarioViewSet, basename="Funcionario")

urlpatterns = [
    path('api/', include(routers.urls)),

    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('produtos/', views.produtos, name='produtos'),

    #Autenticar
    path('conta/login/',views.login, name='login'),
    path('conta/cadastro/', views.cadastro, name='cadastro'),
    path('conta/perfil/', views.perfil, name='perfil'),
    path('conta/logout/', views.logout, name='logout'),

    #TESTE
    path('calendario/', views.calendario, name='calendario'),
    path('dm/painel/horarios/', views.gerenciar_horarios, name='horarios'),

    #Painel admnistrativo
    path('dm/painel/', views.painel, name='painel'),

    path('dm/painel/usuarios/funcionario/', views.tabela_funcionario, name='tabela_funcionario'),
    path('dm/painel/usuarios/funcionario/<int:pk>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('dm/painel/usuarios/funcionario/criar/', views.criar_funcionario, name='criar_funcionario'),
    path('dm/painel/usuarios/funcionario/<int:pk>/editar/', views.editar_funcionario, name='editar_funcionario'),
    path('dm/painel/usuarios/funcionario/<int:pk>/deletar/', views.deletar_funcionario, name='deletar_funcionario'),

    path('dm/painel/usuarios/clientes/', views.tabela_cliente, name='tabela_cliente'),
    path('dm/painel/usuarios/clientes/<int:pk>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('dm/painel/usuarios/clientes/criar/', views.criar_cliente, name='criar_cliente'),
    path('dm/painel/usuarios/clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('dm/painel/usuarios/clientes/<int:pk>/deletar/', views.deletar_cliente, name='deletar_cliente'),

    path('dm/painel/usuarios/produto/', views.tabela_produto, name='tabela_produto'),
    path('dm/painel/usuarios/produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('dm/painel/usuarios/produto/criar/', views.criar_produto, name='criar_produto'),
    path('dm/painel/usuarios/produto/<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('dm/painel/usuarios/produto/<int:pk>/deletar/', views.deletar_produto, name='deletar_produto'),

    path('dm/painel/usuarios/servico/', views.tabela_servico, name='tabela_servico'),
    path('dm/painel/usuarios/servico/<int:pk>/', views.detalhe_servico, name='detalhe_servico'),
    path('dm/painel/usuarios/servico/criar/', views.criar_servico, name='criar_servico'),
    path('dm/painel/usuarios/servico/<int:pk>/editar/', views.editar_servico, name='editar_servico'),
    path('dm/painel/usuarios/servico/<int:pk>/deletar/', views.deletar_servico, name='deletar_servico'),

    path('dm/painel/tabela-agendamentos/', views.tabela_agendamentos, name='tabela_agendamentos'),
    path('dm/painel/criar-agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('dm/painel/deletar_agendamento/<int:agendamento_id>/', views.deletar_agendamento, name='deletar_agendamento'),
    path('dm/painel/editar-agendamento/<int:agendamento_id>/', views.editar_agendamento, name='editar_agendamento'),

    path('dm/painel/usuarios/editar-usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),


    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
    path('dm/painel/perfil/', views.admin_perfil, name='admin_perfil')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

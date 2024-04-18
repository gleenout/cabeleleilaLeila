from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ClienteForm, FuncionarioForm, ProdutoForm, ServicoForm, UsuarioForm
from .models import Produto, Funcionario, Cliente, Servico, User
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.urls import reverse

#========TESTE==============
def is_staff_check(user):
    return user.is_staff
def acesso_negado(request):
    return HttpResponse('Acesso Negado! 💀')
def staff_required(view_func):
    decorated_view = login_required(user_passes_test(is_staff_check, login_url='/acesso-negado/')(view_func))
    return decorated_view
def generate_random_pk():
    return get_random_string(length=5, allowed_chars='0123456789')
#============================

def home(request):
    return render(request, 'home.html')
def servicos(request):
  return render(request,  'servicos.html')
def agendamento(request):
    return render(request, 'agendamento.html')
def produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos.html')

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.data_criacao = timezone.now()
            cliente.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    else:
        form = ClienteForm()
    return render(request, 'auth/cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    if request.method=='POST':
        do_logout(request)
        messages.success(request, 'Você saiu')
        return redirect('login')
    else:
        return render(request, 'home.html')

@login_required(login_url="/conta/login")
def perfil(request):
    return render(request, 'auth/perfil.html')

@staff_required
def painel(request):
    return render(request, 'painel/dm_painel.html')

#==========FUNCIONARIO==========
@staff_required
def tabela_funcionario(request):
    funcionarios= Funcionario.objects.all()
    return render(request, 'painel/tabela_ufuncionario.html', {'funcionarios': funcionarios})

@staff_required
def detalhe_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'painel/tabela_ufuncionario_detalhes.html', {'funcionario': funcionario})
@staff_required
def criar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST, request.FILES)
        form_usuario = UsuarioForm(request.POST)
        if form_funcionario.is_valid() and form_usuario.is_valid():
            funcionario = form_funcionario.save()
            usuario = form_usuario.save(commit=False)
            usuario.set_password(form_usuario.cleaned_data['password'])
            usuario.save()
            funcionario.usuario = usuario
            funcionario.save()
            return redirect('tabela_funcionario')
    else:
        form_funcionario = FuncionarioForm()
        form_usuario = UsuarioForm()
    return render(request, 'painel/tabela_ufuncionario_form.html', {'form_funcionario': form_funcionario, 'form_usuario': form_usuario})

@staff_required
def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if funcionario.usuario:
            form_usuario = UsuarioForm(request.POST, instance=funcionario.usuario)
        else:
            form_usuario = UsuarioForm(request.POST)
        if form_funcionario.is_valid() and form_usuario.is_valid():
            funcionario = form_funcionario.save()
            if funcionario.usuario:
                usuario = form_usuario.save(commit=False)
                usuario.set_password(form_usuario.cleaned_data['password'])
                usuario.save()
                funcionario.usuario = usuario
            else:
                usuario = form_usuario.save()
                funcionario.usuario = usuario
            funcionario.save()
            return redirect('tabela_funcionario')
    else:
        form_funcionario = FuncionarioForm(instance=funcionario)
        if funcionario.usuario:
            form_usuario = UsuarioForm(instance=funcionario.usuario)
        else:
            form_usuario = UsuarioForm()
    return render(request, 'painel/tabela_ufuncionario_form.html', {'form_funcionario': form_funcionario, 'form_usuario': form_usuario})

@staff_required
def deletar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('tabela_funcionario')
    return render(request, 'painel/tabela_ufuncionario_deletar.html', {'funcionario': funcionario})
#==========FUNCIONARIO==========

#==========CLIENTE==========
@staff_required
def tabela_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'painel/tabela_uclientes.html', {'clientes': clientes})

@staff_required
def detalhe_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'painel/tabela_uclientes_detalhes.html', {'cliente': cliente})

@staff_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabela_cliente')
    else:
        form = ClienteForm()
    return render(request, 'painel/tabela_uclientes_form.html', {'form': form})

@staff_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('tabela_cliente')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'painel/tabela_uclientes_form.html', {'form': form})

@staff_required
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('tabela_cliente')
    return render(request, 'painel/tabela_uclientes_delete.html', {'cliente': cliente})
#==========CLIENTE==========

#==========USUÁRIO==========
@staff_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('tabela_funcionario')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'painel/usuario_form.html', {'form': form, 'usuario': usuario})
#==========USUÁRIO==========

#==========PRODUTOS==========
@staff_required
def tabela_produto(request):
    produtos= Produto.objects.all()
    return render(request, 'painel/tabela_produto.html', {'produtos': produtos})

@staff_required
def detalhe_produto(request, pk):
    produto = get_object_or_404(Servico, pk=pk)
    return render(request, 'painel/tabela_produto_detalhes.html', {'produto': produto})

@staff_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabela_produto')
    else:
        form = ProdutoForm()
    return render(request, 'painel/tabela_produto_form.html', {'form': form})

@staff_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('tabela_produto')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'painel/tabela_produto_form.html', {'form': form})

@staff_required
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('tabela_produto')
    return render(request, 'painel/tabela_produto_deletar.html', {'produto': produto})
#==========PRODUTOS==========

#==========SERVIÇOS==========
@staff_required
def tabela_servico(request):
    servicos= Servico.objects.all()
    return render(request, 'painel/tabela_servico.html', {'servicos': servicos})

@staff_required
def detalhe_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    return render(request, 'painel/tabela_servico_detalhes.html', {'servico': servico})

@staff_required
def criar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabela_servico')
    else:
        form = ServicoForm()
    return render(request, 'painel/tabela_servico_form.html', {'form': form})

@staff_required
def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, request.FILES, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('tabela_servico')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'painel/tabela_servico_form.html', {'form': form})

@staff_required
def deletar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('tabela_servico')
    return render(request, 'painel/tabela_servico_deletar.html', {'servico': servico})
#==========SERVIÇOS==========

@staff_required
def admin_perfil (request):
    return render(request, 'painel/dm_perfil.html')

def newlogin (request):
    return render(request, 'auth/new_login.html')

import calendar
from datetime import datetime
def calendario(request, ano=datetime.now().year, mes=datetime.now().strftime('%B').lower()):
    mes = mes.capitalize()
    calendario_mes = calendar.monthcalendar(ano, list(calendar.month_name).index(mes))

    return render(request, 'calendario/calendario.html', {'ano': ano, 'mes': mes, 'calendario_mes': calendario_mes})





from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ClienteForm
from .models import Produto, Funcionario, Cliente, Servico
from django.utils import timezone

def is_staff_check(user):
    return user.is_staff
def acesso_negado(request):
    return HttpResponse('Acesso Negado! 💀')
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

@login_required(login_url="/conta/login")
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def painel(request):
    return render(request, 'painel/painel.html')

@login_required(login_url="/conta/login")
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def tab_usuarios(request):
    funcionarios = Funcionario.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'funcionarios': funcionarios,
        'clientes': clientes,
    }
    return render(request, 'painel/tabela_usuarios.html', context)

@login_required(login_url="/conta/login")
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def tab_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'painel/tabela_produtos.html', context)

@login_required(login_url="/conta/login")
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def tab_servicos(request):
    servicos = Servico.objects.all()
    context = {
        'servicos': servicos,
    }
    return render(request, 'painel/tabela_servicos.html', context)

@login_required(login_url="/conta/login")
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def admin_perfil (request):
    return render(request, 'painel/profile.html')




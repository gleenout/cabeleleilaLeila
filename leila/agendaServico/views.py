from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ClienteForm
from .models import Produto, Funcionario, Cliente
from django.utils import timezone

def is_staff_check(user):
    return user.is_staff
def acesso_negado(request):
    return HttpResponse('Acesso Negado! 💀')

# Create your views here.
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
    '''if request.user.is_authenticated:
        return redirect('perfil')
    if request.method == 'GET':
        return render(request, 'auth/cadastro.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuario com o mesmo nome')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('login')'''
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
    """
    View para autenticação de usuários.

    Se o usuário já estiver autenticado, redireciona para a página de perfil.
    Se o método da requisição for GET, renderiza a página de login.
    Se o método da requisição for POST, tenta autenticar o usuário.

    # Se o usuário já estiver autenticado, redirecione para a página de perfil
    if request.user.is_authenticated:
        return redirect('perfil')
    # Se o método da requisição for GET, renderiza a página de login
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        # Se o método da requisição for POST, tenta autenticar o usuário
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        print(username)
        print(senha)

        if user:
            # Se o usuário for autenticado com sucesso, faça login e redirecione para a página de perfil
            login_django(request, user)
            messages.success(request, 'Você fez login com sucesso!')
            return redirect('perfil')
            #return HttpResponse('Usuario logado')
        else:
            # Se a autenticação falhar, exiba uma mensagem de erro
            mensagem_erro = "Usuário ou senha inválidos"
            return render(request, 'auth/login.html', {'mensagem_erro': mensagem_erro})"""
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
@login_required(login_url="/login")
def plataforma(request):
    return HttpResponse('Voce esta logado')

def logout(request):
    if request.method=='POST':
        do_logout(request)
        messages.success(request, 'Você saiu')
        return redirect('login')
    else:
        return render(request, 'home.html')

@login_required
def perfil(request):
    return render(request, 'auth/perfil.html')

@login_required
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def painel(request):
    #if request.user.is_staff:
    return render(request, 'painel/painel.html')
    #else:
        # Redirecionar para outra página ou exibir uma mensagem de acesso negado
        #return HttpResponse('Acesso Negado! 💀')

@login_required
@user_passes_test(is_staff_check, login_url='/acesso-negado/')
def usuarios(request):
    funcionarios = Funcionario.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'funcionarios': funcionarios,
        'clientes': clientes,
    }
    return render(request, 'painel/tabela_usuarios.html', context)

def tab_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'painel/tabela_produtos.html', context)




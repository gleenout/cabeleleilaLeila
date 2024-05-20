from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ClienteForm, FuncionarioForm, ProdutoForm, ServicoForm, UsuarioForm, AgendamentoForm, HorarioForm
from .models import Produto, Funcionario, Cliente, Servico, User, Agendamento, Horario
from django.utils import timezone

#========TESTE==============
def is_staff_check(user):
    return user.is_staff
def acesso_negado(request):
    return HttpResponse('Acesso Negado! 💀')
def staff_required(view_func):
    decorated_view = login_required(user_passes_test(is_staff_check, login_url='/acesso-negado/')(view_func))
    return decorated_view
#============================

def home(request):
    return render(request, 'home.html')
def servicos(request):
    servicos = Servico.objects.all()
    return render(request,  'servicos.html', {'servicos': servicos})
def produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos.html', context)

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

@login_required(login_url="/conta/login")
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

@staff_required
def painel_perfil(request):
    return render(request, 'painel/dm_perfil.html')

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

#==========AGENDAMENTOS==========
@staff_required
def tabela_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    context = {'agendamentos': agendamentos}
    return render(request, 'painel/tabela_agendamentos.html', context)


def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabela_agendamentos')  # Redireciona para a tabela de agendamentos após salvar
    else:
        form = AgendamentoForm()

    return render(request, 'painel/tabela_agendamento_form.html', {'form': form})

@staff_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('tabela_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'painel/tabela_agendamento_form.html', {'form': form})

def deletar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('tabela_agendamentos')
    return render(request, 'painel/tabela_agendamento_delete.html', {'agendamento': agendamento})
#==========AGENDAMENTOS==========

@staff_required
def admin_perfil (request):
    return render(request, 'painel/dm_perfil.html')

def gerenciar_horarios(request):
    horarios = Horario.objects.all()
    form = HorarioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gerenciar_horarios')

    context = {
        'horarios': horarios,
        'form': form,
    }
    return render(request, 'painel/gerenciar_horarios.html', context)

@login_required
def calendario(request):
    agendamentos = Agendamento.objects.all()
    form = AgendamentoForm()
    horarios_disponiveis = Horario.objects.all()

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.pop('data')
            horario = form.cleaned_data.pop('horario')
            servico = form.cleaned_data.pop('servico')

            agendamento = Agendamento.objects.create(
                data=data,
                horario=horario,
                servico=servico,
                usuario=request.user
            )

            return redirect('calendario')

    return render(request, 'calendario/calendario.html', {'agendamentos': agendamentos, 'form': form, 'horarios_disponiveis': horarios_disponiveis})

@login_required
def apagar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, usuario=request.user)
    agendamento.delete()
    return redirect('calendario')
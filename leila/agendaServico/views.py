from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
  return render(request, 'login.html')
def cadastro(request):
  return render(request, 'cadastro.html')
def servicos(request):
  return render(request,  'servicos.html')
def agendamento(request):
    return render(request, 'agendas.html')
def produtos(request):
    return render(request, 'produtos.html')
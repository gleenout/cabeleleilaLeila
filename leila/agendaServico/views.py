from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')
def servicos(request):
  return render(request,  'servicos.html')
def agendamento(request):
    return render(request, 'agendamento.html')
def produtos(request):
    return render(request, 'produtos.html')
@login_required
def profile(request):
    return render(request, 'perfil.html')





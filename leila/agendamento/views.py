from django.shortcuts import render

# Create your views here.
def agendamento(request):
    return render(request, 'agendas.html')
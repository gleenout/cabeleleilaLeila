from rest_framework import viewsets
from .serializers import FuncionarioSerializer, ClienteSerializer
from .models import Funcionario

class FuncionarioViewSet(viewsets.ModelViewSet):
    model = Funcionario
    serializer_class = FuncionarioSerializer
    queryset =  Funcionario.objects.all()
    fields = ['nome', 'email', 'telefone', 'endereco']
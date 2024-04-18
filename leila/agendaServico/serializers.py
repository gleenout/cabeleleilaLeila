from .models import  Funcionario, Cliente, User, Produto, Servico
from rest_framework import serializers

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'telefone', 'cargo', 'data_admissao', 'imagem_perfil']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        class Meta:
            model = Cliente
            fields = ['nome', 'email', 'telefone', 'endereco']
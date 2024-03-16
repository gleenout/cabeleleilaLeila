from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    data_admissao = models.DateField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario', null=True)
    imagem_perfil = models.FileField(upload_to='funcionarios', null=True, blank=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente', null=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    data_criacao = models.DateField(auto_now_add=True)
    imagem_perfil = models.FileField(upload_to='clientes', null=True, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    #preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.DurationField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
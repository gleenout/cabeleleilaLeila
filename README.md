# Cabeleleila leila
Este repositório contém um projeto Django com as seguintes funcionalidades:

- Sistema de autenticação de usuários.
- Cadastro de clientes, funcionários, agendamento, etc.
- Agendamento com a API FullCalendar
- Painel para admintrar clientes, funcionários, agendamentos, etc.

## Pré-requisitos

Para executar este projeto você vai precisar:

- Python 3.6+
- Pip
- Virtualenv (recomendado)
- Conexção com a internet para rodar midia, css e js

## Configurando o ambiente

1. Clone este repositório

```
git clone https://github.com/usuario/meu-projeto-django.git
```

2. Crie um virtualenv

```
python3 -m venv .venv
```
```
.venv/Scripts/activate
```

3. Instale o django e django-allauth

```
pip install django
```
```
pip install dj-static
```
```
pip install djangorestframework
```

## Executando
```
cd leila
```

Com o ambiente configurado, execute as migrações:

```
python manage.py migrate
```

Em seguida, rode o servidor de desenvolvimento:

```
python manage.py runserver
```

Acesse ``http://127.0.0.1:8000/`` no navegador para visualizar o projeto.

Para acesso administrativo do django, ``http://127.0.0.1:8000/admin``.

Para acesso do painel adminstrativo da aplicação, ``http://127.0.0.1:8000/dm/painel``. (Requer usuário Staff)

### Usuários de teste
Cliente Username e senha: ``Cliente123``.

Administrador Username e Senha: ``Admin123``.

### Criar um super usuário
```
py manage.py createsuperuser
```

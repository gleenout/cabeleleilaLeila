# Cabeleleila leila
Este repositório contém um projeto Django com as seguintes funcionalidades:

- Sistema de autenticação de usuários
- Outras a serem implementadas

## Pré-requisitos

Para executar este projeto você vai precisar:

- Python 3.6+
- Pip
- Virtualenv (recomendado)

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
pip install django-allauth
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

Acesse http://localhost:8000 no navegador para visualizar o projeto.

Para acesso administrativo, acesse http://localhost:8000/admin.

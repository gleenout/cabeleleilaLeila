from django.contrib import admin
from .models import Produto, Servico, Funcionario, Cliente, Agendamento, Horario

admin.site.register(Produto)
admin.site.register(Servico)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Agendamento)
admin.site.register(Horario)
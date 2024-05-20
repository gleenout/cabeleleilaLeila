from django import forms
from django.contrib.auth.models import User
from .models import Cliente, Funcionario, Servico, Produto, Agendamento, Horario

class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if field.required:
                field.widget.attrs.update({'required': 'required'})
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco' ]
        widgets = {
            'data_criacao': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        cliente = super().save(commit=False)
        cliente.usuario = user
        if commit:
            cliente.save()
        return cliente

class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if field.required:
                field.widget.attrs.update({'required': 'required'})

    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'telefone', 'cargo', 'data_admissao', 'imagem_perfil']
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'},  format='%Y-%m-%d'),
            'imagem_perfil': forms.FileInput(attrs={'class': 'form-control-file'})
        }
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'estoque', 'imagem_produto']
        widgets = {
            'data_criacao': forms.DateInput(attrs={'type': 'date'}),
            'data_atualizacao': forms.DateInput(attrs={'type': 'date'})
        }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'preco', 'duracao']
        widgets = {
            'data_criacao': forms.DateInput(attrs={'type': 'date'}),
            'data_atualizacao': forms.DateInput(attrs={'type': 'date'})
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['hora_inicio', 'hora_fim']
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'horario', 'servico', 'usuario']
# core/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Escola, Aluno, Professor, Usuario

class EscolaForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'endereco', 'telefone', 'email', 'foto', 'numero_de_alunos', 'numero_de_ambientes', 'area']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'email', 'senha', 'matricula', 'ano', 'escola', 'turma']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'senha', 'tipo_usuario', 'escola', 'departamento']

class AlunoLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
# core/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Professor, Aluno, Escola, Turma, Usuario
from .forms import EscolaForm, AlunoForm, ProfessorForm, AlunoLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    professores = Professor.objects.all()
    alunos = Aluno.objects.all()
    return render(request, 'core/index.html', {'professores': professores, 'alunos': alunos})

def homeAluno(request):
    return render(request, 'core/homeAluno.html')

def cadastraEscola(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Escola cadastrada com sucesso!")
    else:
        form = EscolaForm()
    return render(request, 'core/cadastroEscola.html', {'form': form})

def cadastraUsuario(request):
    form_type = request.GET.get('form_type', 'aluno')  # Use GET para determinar o tipo de formulário

    if request.method == 'POST':
        if form_type == 'aluno':
            form = AlunoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')  # Redireciona para a página de índice após o sucesso
            else:
                print(form.errors)  # Adiciona uma mensagem de erro se o formulário não for válido
        # Adicione lógica para o formulário de professor se necessário
    else:
        if form_type == 'aluno':
            form = AlunoForm()
        else:
            form = None

    escolas = Escola.objects.all()
    turmas = Turma.objects.all()  # Adiciona esta linha para obter as turmas
    return render(request, 'core/TelaCadastro.html', {'form': form, 'escolas': escolas, 'turmas': turmas})

def aluno_login(request):
    if request.method == 'POST':
        form = AlunoLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usename')
            password = form.cleaned_data.get('senha')  # Alterado para 'senha'
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'tipo_usuario') and user.tipo_usuario == 'aluno':
                login(request, user)
                messages.info(request, f"Você está logado como {user.username}.")
                return redirect('homeAluno')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            print(form.errors)  # Adicione esta linha para verificar os erros do formulário
            messages.error(request, "Informações inválidas.")
    else:
        form = AlunoLoginForm()
    return render(request, 'core/index.html', {'form': form})

def aluno_logout(request):
    logout(request)
    messages.info(request, "Você foi desconectado com sucesso.")
    return redirect('aluno_login')

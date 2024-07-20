from django.shortcuts import render
from .models import Professor, Aluno

def index(request):
    professores = Professor.objects.all()
    alunos = Aluno.objects.all()
    return render(request, 'core/index.html', {'professores': professores, 'alunos': alunos})

def cadastro(request):
    

    return render(request, 'core/TelaCadastro.html')

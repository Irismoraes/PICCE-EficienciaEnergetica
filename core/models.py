from django.db import models
import MySQLdb

class Escola(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    foto = models.ImageField(upload_to='escolas/fotos/', null=True, blank=True)
    numero_de_alunos = models.IntegerField()
    numero_de_ambientes = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)  # Área em metros quadrados, por exemplo

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=255)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, default='Desconhecido')
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=[('professor', 'Professor'), ('aluno', 'Aluno')])
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome']

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True

class Professor(Usuario):
    departamento = models.CharField(max_length=255)
    turmas = models.ManyToManyField(Turma, related_name='professores')

class Aluno(Usuario):
    matricula = models.CharField(max_length=20)
    ano = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Ambiente(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Resultado(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    data = models.DateField()
    pontuacao = models.IntegerField()
    observacoes = models.TextField()

    def __str__(self):
        return f'Resultado de {self.aluno.nome} em {self.data}'

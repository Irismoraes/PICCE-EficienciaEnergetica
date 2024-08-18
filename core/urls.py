# core/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('homeAluno/', views.homeAluno, name='homeAluno'),
    path('cadastraEscola/', views.cadastraEscola, name='cadastraEscola'),
    path('cadastraUsuario/', views.cadastraUsuario, name='cadastraUsuario'),
    path('login/', views.aluno_login, name='aluno_login'),
    path('logout/', views.aluno_logout, name='aluno_logout'),
]


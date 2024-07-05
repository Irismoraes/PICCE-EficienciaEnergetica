# core/views.py

from django.shortcuts import render
from .models import Usuario

def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})


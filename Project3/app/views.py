from django.shortcuts import render

from django.http import HttpResponse
from .models import Tarefas

def inicio(request):
    tarefas = Tarefas.objects.all().order_by('status')
    return render(request, 'home.html', {'tarefas':tarefas})

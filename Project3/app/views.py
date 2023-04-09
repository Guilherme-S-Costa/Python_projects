from django.shortcuts import render, redirect

from .models import Tarefas
from .forms import AdicionarTarefa


def listar(request):
    """ Listar Tarefas """
    tarefas = Tarefas.objects.all().order_by('-created_at')  # busca todas as tarefas
    return render(request, 'home.html', {'tarefas': tarefas}) # retorna/renderiza o template para listar as tarefas

def recuperar(request, **kwargs): 
    pk = kwargs.get('pk')
    tarefa = Tarefas.objects.get(pk=pk)
    form = AdicionarTarefa(instance=tarefa)
    context = {'tarefa': tarefa, 'form': form}
    return render(request, 'form_update.html', context)

def adicionar(request):
    """ Registrar uma tarefa no banco de dados """
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)  
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = AdicionarTarefa()

    context = {'form': form}
    return render(request, 'form.html', context)


def atualizar(request, **kwargs):
    """ Atualizar uma tarefa no banco de dados """
    pk = kwargs.get('pk')
    tarefa = Tarefas.objects.get(pk=pk)
    form = AdicionarTarefa(data=request.POST, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('listar')

def deletar(request, **kwargs):
    if pk := kwargs.get('pk'):
        tarefa = Tarefas.objects.get(pk=pk)
        tarefa.delete()
        return redirect('listar')

from django.shortcuts import render, redirect

from .models import Tasks
from .forms import CreateTasks


def list_tasks(request):
    """ Listar Tarefas """
    tasks = Tasks.objects.all().order_by('-created_at')  # busca todas as tarefas
    return render(request, 'home.html', {'tasks': tasks}) # retorna/renderiza o template para listar as tarefas

def retrive(request, **kwargs): 
    pk = kwargs.get('pk')
    task = Tasks.objects.get(pk=pk)
    form = CreateTasks(instance=task)
    context = {'task': task, 'form': form}
    return render(request, 'form_update.html', context)

def create(request):
    """ Registrar uma tarefa no banco de dados """
    if request.method == 'POST':
        form = CreateTasks(data=request.POST)  
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = CreateTasks()

    context = {'form': form}
    return render(request, 'form.html', context)


def update(request, **kwargs):
    """ Atualizar uma tarefa no banco de dados """
    pk = kwargs.get('pk')
    task = Tasks.objects.get(pk=pk)
    form = CreateTasks(data=request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('list_tasks')

def delete(request, **kwargs):
    if pk := kwargs.get('pk'):
        task = Tasks.objects.get(pk=pk)
        task.delete()
        return redirect('list_tasks')

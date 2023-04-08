from django.shortcuts import render, redirect

# from django.http import HttpResponse
from .models import Tarefas
from .forms import AdicionarTarefa

def inicio(request):
    tarefas = Tarefas.objects.all().order_by('status')
    return render(request, 'home.html', {'tarefas': tarefas})


def adicionar(request):
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)  
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AdicionarTarefa()
    return render(request, 'form.html', {'form': form})


def concluir(request):
    return redirect('inicio')


def deletar(request):
    return redirect('inicio')


def editar(request, **kwargs): 
    print(kwargs)
    return render(request, 'form.html')
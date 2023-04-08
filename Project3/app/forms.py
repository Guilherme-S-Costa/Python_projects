from django import forms
from .models import Tarefas
from .choices import OPCOES_PRIORIDADE, OPCOES_STATUS

class AdicionarTarefa(forms.ModelForm):
     content = forms.CharField(max_length=100, label='Titulo da Tarefa')
     priority = forms.CharField(max_length=100, label='Prioridades', widget=forms.Select(choices=OPCOES_PRIORIDADE))
     status = forms.CharField(max_length=100, label='Status', widget=forms.Select(choices=OPCOES_STATUS))

     class Meta:
          model = Tarefas
          fields = ['content', 'priority', 'status']
     
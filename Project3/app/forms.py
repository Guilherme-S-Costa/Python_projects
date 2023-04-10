from django import forms
from .models import Tasks
from .choices import OPTIONS_PRIORITY, OPTIONS_STATUS

class CreateTasks(forms.ModelForm):
     title = forms.CharField(max_length=100, label='Titulo da Tarefa')
     content = forms.CharField(max_length=100, label='Descrição da Tarefa', required=True)
     priority = forms.CharField(max_length=100, label='Prioridade da Tarefa', widget=forms.Select(choices=OPTIONS_PRIORITY))
     status = forms.CharField(max_length=100, label='Status', widget=forms.Select(choices=OPTIONS_STATUS))

     class Meta:
          model = Tasks
          fields = ['title', 'content', 'priority', 'status']
     
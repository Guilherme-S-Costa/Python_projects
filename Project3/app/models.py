from django.db import models

from .choices import OPCOES_PRIORIDADE, OPCOES_STATUS


class Tarefas(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, default='pendente')
    priority = models.CharField(max_length=100, choices=OPCOES_PRIORIDADE, default='importante')

    def __str__(self):
        return f"{self.title}"

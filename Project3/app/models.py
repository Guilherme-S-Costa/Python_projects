from django.db import models

from .choices import OPCOES_CATEGORIA, OPCOES_STATUS


class Tarefas(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, default='pendente')
    category = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='importante')

    def __str__(self):
        return f"{self.title}"

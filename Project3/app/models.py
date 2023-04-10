from django.db import models

from .choices import OPTIONS_PRIORITY, OPTIONS_STATUS


class Tasks(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.CharField(max_length=200, verbose_name='Conteúdo', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Criado em') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    status = models.CharField(max_length=100, choices=OPTIONS_STATUS, default='pending', verbose_name='Pendente')
    priority = models.CharField(max_length=100, choices=OPTIONS_PRIORITY, default='important', verbose_name='Importante')

    def __str__(self):
        return f"{self.title}"

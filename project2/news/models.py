from django.db import models

# Create your models here.
# O modelo representa uma entidade (TABELA) dentro do banco de dados.

class Postagens(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk} | {self.titulo}"

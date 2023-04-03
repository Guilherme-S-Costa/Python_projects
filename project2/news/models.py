from django.db import models

class Postagens(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk} | {self.titulo}"

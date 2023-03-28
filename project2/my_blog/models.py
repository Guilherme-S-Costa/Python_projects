import datetime

from django.db import models
from django.util import timezone

# Create your models here.
class Questao(models.Model):
    # texto = models.CharField(max_length=215)
    # data_pub = models.DateTimeField('data de publicação')
    # def __str__(self):
    #     return self.texto
    def was_published__recently(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)        

class Opcao(models.Model):
    # questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    # texto_opc = models.CharField(max_length=200)
    # votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_opc

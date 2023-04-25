import re

from django.db import models
from django.contrib.auth.models import User

from django.forms import ValidationError

from app import utils

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Nome do Usuaŕio')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Data de nascimento')
    document = models.CharField(max_length=11, verbose_name='Documento', null=True, blank=True)
    address = models.JSONField(verbose_name='Endereço', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de usuário'
        verbose_name_plural = 'Perfis de usuários'

    def __str__(self) -> str:
        name = self.user.first_name
        if not name:
            name = self.user
        return name
    
    def clean(self) -> None:
        error_messages = {} 

        if not utils.valida_cpf(self.document):
            error_messages['document'] = 'Digite um numero de CPF válido'

        if self.address and 'cep' in self.address.keys():
            cep = self.address.get('cep')
            if re.search(r'[^0-9]', cep) or len(cep) <8:
                error_messages['cep'] = 'CEP inválido, por gentileza, digite um numero de CEP válido'

        if error_messages:
            raise ValidationError(error_messages)

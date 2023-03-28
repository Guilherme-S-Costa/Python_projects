from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .models import Postagens

# Create your views here.
def jornal(request):

    # postagens = Postagens.objects.all()
    # for postagem in postagens:
        # print(postagem)
        # print(postagem.titulo)
        # print(postagem.data)
        # print(postagem.conteudo)

    # select * from Postagens
    postagens = Postagens.objects.all()
    templates = loader.get_template('news/templates/home.html')
    context = {'postagens': postagens}

    return HttpResponse(templates.render(context, request))



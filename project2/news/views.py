from django.http import HttpResponse
from django.template import loader 

from .models import Postagens

def jornal(request):
    postagens = Postagens.objects.all().values()
    templates = loader.get_template('home.html')        
    context = {'postagens': postagens}

    return HttpResponse(templates.render(context, request))

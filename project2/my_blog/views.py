from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def visual(request):
    template = loader.get_template('myfirts.html')
    return HttpResponse(template.render())

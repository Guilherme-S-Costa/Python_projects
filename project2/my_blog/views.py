from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def visual(request):
    return HttpResponse('Esse é o blog do momento')

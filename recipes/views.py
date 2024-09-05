from django.http import HttpResponse

# from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return HttpResponse('do arquivo views.py')
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse('contato')
def sobre(request):
    return HttpResponse('sobre')
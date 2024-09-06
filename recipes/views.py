from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Will Avelar',
    })


def contato(request):
    return HttpResponse('contato')
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
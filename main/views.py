from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница',
        'list':['first', 'second'],
        'dict':{'first':1},
        'is_authenticated':False
    }
    return render(request, 'base.html', context)

from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    my_dict = {'inster_me': "Hello I am from views.py!!"}
    return render(request, 'index.html', context=my_dict)

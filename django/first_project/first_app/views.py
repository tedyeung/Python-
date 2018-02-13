from django.shortcuts import render
from djago.http import HttpResponse 

def index(request):
    return HttpResponse("Slavo your first Django Project")

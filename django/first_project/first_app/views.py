from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = { 'insert' : "Hello I am from views.py!!"}
    return render(request, 'index.html', context=my_dict)

from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    my_dict = {
        'text': 'Well Done Slavo!! You did it!!!'
    }
    return render(request, 'help.html', context=my_dict)

def test(request):
    return render(request, 'test.html')
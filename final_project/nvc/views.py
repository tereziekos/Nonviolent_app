from django.shortcuts import render
from .models import Feeling
from django.http import HttpResponse
from django.template import loader



def homepage(request):
    return render(request, 'nvc/homepage.html')

def feelings_inventory(request):
    feelings = Feeling.objects.all()
    inventory=  {'feelings': feelings}
    return render(request,'nvc/feelings.html', inventory)
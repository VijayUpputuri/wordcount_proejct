from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def egg(request):
    return HttpResponse('egg is good food') 
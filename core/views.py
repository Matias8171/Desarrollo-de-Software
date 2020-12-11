from django.http import request
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"core/home.html")

def acercade(request):
    return render(request,"core/acercade.html")

def servicios(request):
    return render(request,"core/servicios.html")
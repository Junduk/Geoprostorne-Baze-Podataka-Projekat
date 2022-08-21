from django.http import request
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def pocetna(request):
    return render(request, 'pocetna.html')

def d3prikaz(request):
    return render(request, '3dprikaz.html')

def d2prikaz(request):
    return render(request, '2dprikaz.html')

def about(request):
    return render(request, 'about')
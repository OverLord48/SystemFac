from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.erp.models import *

# Create your views here.

def myfirstview(request):
    data = {
        'name': 'Cesar',
        'categorias': Categorias.objects.all()
    }
    return render(request, 'index.html', data)

def mysecondview(request):
    
    productos = Productos.objects.all()

    data = {
        'name': 'Antonio',
        'productos': productos
    }
    return render(request, 'home.html', data)
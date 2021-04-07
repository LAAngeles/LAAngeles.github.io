from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Se crea una función para recibir un argumento de http
def index(request):
    return HttpResponse("Hello, word")
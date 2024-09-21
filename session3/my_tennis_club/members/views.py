from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def register(request):
    return render(request, 'register.html')

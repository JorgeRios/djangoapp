from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello this is index")

def test(request):
    return HttpResponse("hello this is test")
# Create your views here.

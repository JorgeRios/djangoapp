from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    html = "<html><body>It is now {}.</body></html>".format(now)
    return HttpResponse(html)

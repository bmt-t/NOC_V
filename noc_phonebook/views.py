from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def phones(request):
    return HttpResponse("tribm: 0963324864")
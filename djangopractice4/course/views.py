from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def learn_dj(request):
    return HttpResponse('learn django')

def learn_py(request):
    return HttpResponse('learn python')
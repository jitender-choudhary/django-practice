from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_dj(request):
    return HttpResponse('django course fees = 300')

def fees_py(request):
    return HttpResponse('python course fees = 400')


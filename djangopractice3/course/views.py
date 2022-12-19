from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("helllo django")


def home(request):
    return HttpResponse("Hello python")

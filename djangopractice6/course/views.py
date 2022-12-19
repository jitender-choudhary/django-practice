from django.shortcuts import render

# Create your views here.
def learncourse(request):
    return render(request,'course/courseone.html')
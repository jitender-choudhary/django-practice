from django.shortcuts import render
from datetime import datetime
# Create your views here.

def feesdj(request):
   
    return render(request, 'fees/feesone.html', {'nm' : 'Django', 'st' : 5})
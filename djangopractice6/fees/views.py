from django.shortcuts import render

# Create your views here.
def coursefees(request):
    return render(request,'fees/feesone.html')
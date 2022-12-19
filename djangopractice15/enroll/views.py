from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def registration(request):
    if request.method=='POST':
        fm =StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'your account has been created')
            messages.info(request, 'now you can login')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html',{'form': fm})


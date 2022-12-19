from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
#sign up view
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'account created successfully')
            fm.save()

    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form' : fm})


# login view
def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request = request, data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            unpass = fm.cleaned_data['password']
            user = authenticate(username =uname, password = unpass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form' : fm})



# profile view
def user_profile(request):
    return render(request, 'enroll/profile.html')

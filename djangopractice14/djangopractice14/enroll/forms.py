from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name': 'enter the name', 'password' : 'enter the password', 'email': 'enter the email'}
        error_messages = {'name': {'required': 'name is mandatory'}}
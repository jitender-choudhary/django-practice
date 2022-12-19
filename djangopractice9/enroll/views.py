from django.shortcuts import render
from enroll.models import Student

def studentinfo(request):
    stud = Student.objects.get(pk=2)
    return render(request, 'enroll/studetails.html', {'stu' : stud})
from django.contrib import admin

# Register your models here.
from enroll.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id', 'stuid', 'stuname', 'stuemail', 'stupass')
#admin.site.register(Student,StudentAdmin)
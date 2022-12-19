from django.urls import path
from . import views

urlpatterns = [
    path('coursedj/', views.fees_django),]
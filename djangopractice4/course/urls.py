from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('learndj/', views.learn_dj),
    path('learnpy/',views.learn_py),
]

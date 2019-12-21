from django.contrib import admin
from django.urls import path
from . import views

app_name='boards'

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('home/<int:pk>/',views.work_view,name='work'),
    path('home/new/',views.make_package,name='make_package'),
    path('home/<int:pk>/add/',views.make_work,name='make_work'),
    path('home/<int:pk>/done/',views.done,name='done'),
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('registration',views.registration,name='registration'),
    path('Artists',views.Artists,name='Artists'),
    
]
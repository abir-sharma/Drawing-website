# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from datetime import date, datetime
from Home.models import Artistss
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .form import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == "POST":
        form = ArtistssForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been addesd successfully.')

    else:
        form = ArtistssForm()
        # name=request.POST['name']
        # desc=request.POST['Description']
        # city=request.POST['city']
        # time=request.POST['time']
        # i_d=request.POST['instagram']
        # price=request.POST['price']
        # img1=request.POST['first_image']
        # img2=request.POST['second_image']
        # img3=request.POST['third_image']
        # availaible=request.POST['available']
        # if availaible=='YES':
        #     availaible=True
        # else:
        #     availaible=False
        # Art_reg=Artistss(name=name,desc=desc,city=city,time=time,i_d=i_d,price=price,img1=img1,img2=img2,img3=img3,availaible=availaible)
        # Art_reg.save()
        # messages.success(request, 'You have been addesd successfully.')
    return render(request,'registration.html',{'form':form })

def Artists(request):
    arti=Artistss.objects.all()
    return render(request,'Artists.html',{'arti':arti})



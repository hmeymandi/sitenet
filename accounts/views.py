from django.contrib.messages.api import success
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login as auth_login,logout as django_logout
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect("account:home")
    else:
        form=Userloginform()
        if request.method=='POST':
            form=Userloginform(request.POST) 
            if form.is_valid():
                data=form.cleaned_data
                user=authenticate(request,idcart=data['idcart'],password=data['password'])
                if user is not None:
                    auth_login(request, user)
                    messages.success(request,'با موفقیت وارد شدید',extra_tags='success')
                    return redirect('net:listreport')
                else:
                    messages.success(request,'نام کاربری و پسورد شما اشتباه است',extra_tags='danger')

            
        else:
            form=Userloginform()
        
    return render(request,'login.html',{'form':form})


def logout(request):
    django_logout(request)
    messages.success(request,'با موفقیت خارج شدید',extra_tags='warning')
    return redirect('account:login')
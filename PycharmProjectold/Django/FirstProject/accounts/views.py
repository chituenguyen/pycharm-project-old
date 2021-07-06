from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import NameForm
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'User taken')
                return redirect('/accounts/register')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('/accounts/register')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('/travel')
        else:
            messages.info(request,'password wrong')
            return redirect('/accounts/login')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/travel')
        else:
            messages.info(request,'invalid')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/travel')



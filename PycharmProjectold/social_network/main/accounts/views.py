from django.shortcuts import render, HttpResponse, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'accounts/sign up.html')


def signup(request):
    if request.method == 'POST':
        mail = request.POST.get('Email', '')
        username = request.POST.get('Username', '')
        name = request.POST.get('Name', '')
        password = request.POST.get('Password', '')
        confirm_password = request.POST.get('ConfirmPassword', '')

        userCheck=User.objects.filter(username=username)
        if userCheck:
            messages.error(request,'username taken')
            return redirect('/')

        if password == confirm_password:
            user_obj = User.objects.create_user(first_name=name, password=password, email=mail, username=username)
            user_obj.save()

    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('usernamelogin', '')
        password = request.POST.get('passwordlogin', '')

        userlogin = authenticate(request, username=username, password=password)
        if userlogin is not None:
            dj_login(request, userlogin)
            messages.success(request, 'login success')
            return redirect('/userpage')
        else:
            messages.error(request, 'fail')
            return redirect('/')


def logout(request):
    dj_logout(request)
    return redirect('/')

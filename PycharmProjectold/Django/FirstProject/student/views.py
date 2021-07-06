from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'tue'})
def add(request):
    val1=(request.POST['num1'])
    val2=(request.POST['num2'])
    if val1=='' or val2=='':
        res='back and input again'
    else:
        res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})

def travel(request):
    dests=Destination.objects.all()

    return render(request,'travel.html',{'dests':dests})
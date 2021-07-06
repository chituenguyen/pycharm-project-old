from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.core.mail import send_mail


from .models import Employee
# Create your views here.
def home(request):
    # return HttpResponse('<h1>welcome homepage</h1>')
    employees=Employee.objects.all()
    return render(request,'home.html',{'employees':employees})



def employee_data(request,employee_id):
    # return HttpResponse(f'ID: {employee_id}')
    try:
        emplyee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found')
    return render(request,'employee_data.html',{'employee':emplyee})

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)



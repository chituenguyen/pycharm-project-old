from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.http import Http404


# Create your views here.

def home(request):
    # return HttpResponse('welcome home')
    Students = student.objects.all()
    return render(request, 'home.html', {'Students': Students})


def student_detail(request, student_id):
    # return HttpResponse(f'student_id {student_id}')  #f ?? what mean??
    try:
        students = student.objects.get(id=student_id)
    except student.DoesNotExist:
        raise Http404('no found')
    return render(request, 'data_students.html', {'students': students})

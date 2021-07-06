from django.db import models
from datetime import datetime

# Create your models here.

# In here, create class ...
class student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    status = [
        (0, 'di hoc'),
        (1, 'di lam')
    ]

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,blank=True)
    email_id=models.EmailField(max_length=255)
    phone_number=models.CharField(max_length=13)
    date_of_birth = models.DateField(default=datetime.now)
    student_gender = models.CharField(choices=GENDER_CHOICES, max_length=1,blank=True)
    student_status=models.IntegerField(choices=status,max_length=1,default=1)




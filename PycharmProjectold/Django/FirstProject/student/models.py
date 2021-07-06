from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    birthday=models.DateField()
    email=models.EmailField(max_length=100)
    student_class=models.ManyToManyField('course',blank=True)

    def course_student(self):
        return "\n".join([p.name for p in self.student_class.all()])

class course(models.Model):
    name=models.CharField(max_length=10)
    option_choice=[('0','onl'),('1','off')]
    type=models.CharField(choices=option_choice,max_length=1,blank=True)
    def __str__(self):
        return self.name

class Destination(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

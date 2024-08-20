from django.db import models
from course.models import Course
from classes.models import Classes

# Create your models here.

class Teacher(models.Model):
    teacher_age=models.SmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.AutoField(primary_key=True)
    teacher_course=models.CharField(max_length=20)
    teacher_contact=models.CharField(max_length=20)
    teacher_description=models.TextField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.SmallIntegerField()
    teacher_headshot=models.ImageField(upload_to='images/')
    teacher_bank_account=models.IntegerField()
    course=models.ManyToManyField(Course, related_name='teachers')
    classes=models.ManyToManyField(Classes, related_name='teachers')

    
    def __str__(self):
        return f'{self.teacher_description} {self.teacher_age}'

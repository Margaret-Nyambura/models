from django.db import models
from student.models import Student
from teacher.models import Teacher

# Create your models here.

class Teacher(models.Model):
    teacher_age=models.SmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.SmallIntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_contact=models.CharField(max_length=20)
    teacher_description=models.TextField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.SmallIntegerField()
    teacher_headshot=models.ImageField(upload_to='images/')
    teacher_bank_account=models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ManyToManyField(Course, related_name='teachers')
    classes=models.ManyToManyField(Classes, related_name='teachers')

    
    def __str__(self):
        return f'{self.teacher_description} {self.teacher_age}'

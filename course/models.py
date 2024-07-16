from django.db import models
from student.models import Student


# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_code=models.IntegerField()
    course_TA=models.CharField(max_length=20)
    course_term=models.CharField(max_length=20)
    course_description=models.TextField()
    course_department=models.CharField(max_length=20)
    course_syllabus=models.CharField(max_length=20)
    course_instructor=models.CharField(max_length=20)
    course_duration=models.SmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.course_assignment} {self.course_department}"


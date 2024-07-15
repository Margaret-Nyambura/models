from django.db import models
from student.models import Student


# Create your models here.

class Period(models.Model):
    start_time=models.SmallIntegerField()
    end_time=models.SmallIntegerField()
    course=models.CharField(max_length=20)
    classroom=models.CharField(max_length=20)
    day_of_the_week=models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


def __str__(self):
    f"{self.classroom} {self.end_time}"

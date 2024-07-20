from django.db import models
from student.models import Student


# Create your models here.


class Period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    day_of_the_week = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.start_time} {self.end_time}"
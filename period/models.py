from django.db import models

class Period(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    course = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    day_of_the_week = models.IntegerField()
    classes = models.ForeignKey('classes.Classes', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE)

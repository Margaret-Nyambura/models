from django.db import models


# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_id=models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=10, unique=True)
    course_TA=models.CharField(max_length=20)
    course_term=models.CharField(max_length=20)
    course_description=models.TextField()
    course_department=models.CharField(max_length=20)
    course_syllabus=models.CharField(max_length=20)
    course_instructor=models.CharField(max_length=20)
    course_duration=models.SmallIntegerField()


def __str__(self):
    return f"{self.course_assignment} {self.course_department}"


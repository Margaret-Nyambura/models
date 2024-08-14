from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classes.models import Classes
from period.models import Period

class StudentSerializer(serializers.ModelSerializer):
       class Meta:
              model=Student
              fields="__all__"


class TeacherSerializer(serializers.ModelSerializer):
       class Meta:
              model=Teacher
              fields="__all__"


class CourseSerializer(serializers.ModelSerializer):
       class Meta:
              model=Course
              fields="__all__"


class ClassesSerializer(serializers.ModelSerializer):
       class Meta:
              model=Classes
              fields="__all__"

class PeriodSerializer(serializers.ModelSerializer):
       class Meta:
              model=Period
              fields="__all__"

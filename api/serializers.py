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
              
class StudentSerializer(serializers.ModelSerializer):
       course=CourseSerializer(many=True)
       class Meta:
              model=Student
              fields="__all__"


class ClassesSerializer(serializers.ModelSerializer):
       class Meta:
              model=Classes
              fields="__all__"
              


class PeriodSerializer(serializers.ModelSerializer):
       class Meta:
              model=Period
              fields="__all__"
              

class MinimalStudentSerializer(serializers.ModelSerializer):
       full_name=serializers.SerializerMethodField()
       def get_full_name(self,object):
              return f"{object.first_name} {object.last_name}"
       
       class Meta:
              model=Student
              fields=["full_name","email","student_id"]
    
class MinimalTeacherSerializer(serializers.ModelSerializer):
       teacher_age=serializers.SerializerMethodField()
       def get_teacher_age(self,object):
              return f"{object.teacher_name} {object.teacher_contact}"
       
       class Meta:
              model=Teacher
              fields=["teacher_id", "teacher_contact","teacher_course","teacher_age"]
              
              
class MinimalCourseSerializer(serializers.ModelSerializer):
       course_id=serializers.SerializerMethodField()
       def get_course_id(self,object):
              return f"{object.course_duration} {object.course_instructor}"
       
       class Meta:
              model=Course
              fields=["course_duration","course_id","course_instructor"]
              
class MinimalClassesSerializer(serializers.ModelSerializer):
       class_id=serializers.SerializerMethodField()
       def get_class_id(self,object):
              return f"{object.class_table_number} {object.class_description}"
       
       class Meta:
            model=Classes
            fields=["class_table_number", "class_bio", "class_id", "class_description"]
       
class MinimalPeriodSerializer(serializers.ModelSerializer):
       start_time=serializers.SerializerMethodField()
       def get_start_time(self,object):
              return f"{object.end_time} {object.classroom}"
       class Meta:
           model=Period
           fields=["start_time", "end_time", "classes","teacher"]
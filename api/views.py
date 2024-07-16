from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from course.models import Course
from .serializers import CourseSerializer
from classes.models import Classes
from .serializers import ClassesSerializer
from period.models import Period
from .serializers import PeriodSerializer


# Create your views here.

class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)


class TeacherListView(APIView):
    def get(self,request):
        teachers=Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self,request,format=None):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)


class ClassListView(APIView):
    def get(self,request,format=None):
        classess=Classes.objects.all()
        serializer=ClassesSerializer(classess,many=True)
        return Response(serializer.data)

class PeriodListView(APIView):
    def get(self,request,format=None):
        periods=Period.objects.all()
        serializer=PeriodSerializer(periods,many=True)
        return Response(serializer.data)

    



from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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
        first_name=request.query_params.get("first_name")
        if first_name:
            students=students.filter(first_name=first_name)
        country=request.query_params.get("country")
        if country:
            students=students.filter(country=country)
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
        


    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        serializer=Student.objects.get(id=id)
        Student.delete()
        return Response(status=status.HTTP_201_ACCEPTED)
    
    def enroll_student(self,student,course_id):
        course=Course.objects.get(id=course_id)
        student.courses.add(course)
        
    def enroll_student(self,student,class_id):
        classes=Classes.objects.get(id=class_id)
        student.classes.add(classes)
        
            
    def post(self,request,id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action:"enroll"
        course_id=request.data.get("course")
        self.enroll_student(student,course_id)
        class_id=request.data.get("classes")
        self.enroll_student(student,class_id)
        return Response(status.HTTP_201_ACCEPTED)



class TeacherListView(APIView):
    def get(self,request):
        teachers=Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
    def post(self,request):
          serializer=TeacherSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.errors,status=status.HTTP_201_CREATED)
          else:
              return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        serializer=Teacher.objects.get(id=id)
        Teacher.delete()
        return Response(status=status.HTTP_201_ACCEPTED)
    
    def enroll_teacher(self,teacher,course_id):
        course=Course.objects.get(id=course_id)
        teacher.course.add(courses)
        
    def enroll_teacher(self, teacher,class_id):
        classes=Classes.objects.get(id=class_id)
        teacher.classes.add(Classes)
        
              
    def post(self,request,id):
        teacher=Teacher.objects.get(id=id)
        action=request.data.get("action")
        if action:"enroll"
        course_id=request.data.get("course")
        self.enroll_teacher(teacher,course_id)
        class_id=request.data.get("classes")
        self.enroll_teacher(teacher, class_id)
        return Response(status.HTTP_201_ACCEPTED)
        
    
    
        
class CourseListView(APIView):
    def get(self,request,format=None):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
class CourseDetailView(APIView):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        serializer=Course.objects.get(id=id)
        Course.delete()
        return Response(status=status.HTTP_201_ACCEPTED)


class ClassListView(APIView):
    def get(self,request,format=None):
        classess=Classes.objects.all()
        serializer=ClassesSerializer(classess,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

        
class classDetailView(APIView):
    def get(self,request,id):
        classes=Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes)
        return Response(serializer.data)
    
    def put(self,request,id):
        classes=Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        serializer=Classes.objects.get(id=id)
        Classes.delete()
        return Response(status=status.HTTP_201_ACCEPTED)
    

class PeriodListView(APIView):
    def get(self,request,format=None):
        periods=Period.objects.all()
        serializer=PeriodSerializer(periods,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
class PeriodDetailView(APIView):
    def get(self,request,id):
        period=Period.objects.get(id=id)
        serializer=PeriodSerializer(period)
        return Response(serializer.data)
    def put(self,request,id):
        period=Period.objects.get(id=id)
        serializer=PeriodSerializer(period,data=request.data)
        if serializer.is_valid():
            return Response(serializer.date,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        serializer=Period.objects.get(id=id)
        Period.delete()
        return Response(status=status.HTTP_201_ACCEPTED)
        
        



    

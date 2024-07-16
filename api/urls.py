from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassListView
from .views import PeriodListView

urlpatterns=[
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("classess/", ClassListView.as_view(), name="classes_list_view"),
    path("periods/", PeriodListView.as_view(), name="period_list_view")
]
from django.urls import path
from .views import StudentListView, StudentDetailView
from .views import TeacherListView,TeacherDetailView
from .views import CourseListView,CourseDetailView
from .views import ClassListView,CourseDetailView
from .views import PeriodListView,PeriodDetailView

urlpatterns=[
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path("classess/", ClassListView.as_view(), name="classes_list_view"),
    path("periods/", PeriodListView.as_view(), name="period_list_view"),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path("classes/<int:id>/", CourseDetailView.as_view(), name="classes_detail-view"),
    path("period/<int:id>/", PeriodDetailView.as_view(), name="period_detail_view")
]
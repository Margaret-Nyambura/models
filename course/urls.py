from django.urls import path
from .import views

urlpatterns=[
    path("register/", views.register_course, name="register_course"),
]
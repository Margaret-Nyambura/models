from django.urls import path
from .import views

urlpatterns=[
    path("register/", views.register_classes, name="register_classes"),
]
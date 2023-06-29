from django.urls import path
from .views import index, add_student, student_report

urlpatterns=[
    path('', index),
    path('students/add/', add_student),
    path('students/<int:id>', student_report),
]
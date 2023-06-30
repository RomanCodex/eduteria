from django.urls import path
from .views import index, add_student, student_report

urlpatterns=[
    path('', index),
    path('students/add/', add_student, name="add-student"),
    path('students/<int:id>', student_report, name="student-report"),
]
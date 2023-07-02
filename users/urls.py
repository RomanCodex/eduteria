from django.urls import path
from .views import index, add_student, student_report, all_students, all_teachers

urlpatterns=[
    path('', index),
    path('students/', all_students, name="all-students"),
    path('students/add/', add_student, name="add-student"),
    path('students/<int:id>/', student_report, name="student-report"),
    path('teachers/', all_teachers, name="all-teachers"),
]
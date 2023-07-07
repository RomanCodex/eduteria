from django.urls import path
from .views import index, add_student, student_report, all_students, all_teachers, add_teacher

urlpatterns=[
    path('', index, name='home'),
    path('students/all/', all_students, name="all-students"),
    path('students/add/', add_student, name="add-student"),
    path('students/<int:id>/', student_report, name="student-report"),
    path('teachers/all/', all_teachers, name="all-teachers"),
    path('teachers/add/', add_teacher, name="add-teacher"),
]
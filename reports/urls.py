from django.urls import path
from .views import create_report, all_reports

urlpatterns=[
    path('add/', create_report, name="create-report"),
    path('all/', all_reports, name="all-reports"),
]
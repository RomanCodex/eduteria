from django.urls import path
from .views import add_report, all_reports

urlpatterns=[
    path('add/', add_report, name="add-report"),
    path('all/', all_reports, name="all-reports"),
]
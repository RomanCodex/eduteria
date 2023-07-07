from django.urls import path
from .views import all_payments, add_payment

urlpatterns=[
    path("all/", all_payments, name="all-payments"),
    path("add/", add_payment, name="add-payment"),
]
from django.db import models
from users.models import Student

# Create your models here.
class Payment(models.Model):
    date_of_payment=models.DateTimeField(auto_now_add=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    payment_for=models.CharField(max_length=256)
    payment_by=models.CharField(max_length=256)
    received_by=models.CharField(max_length=256)

    class Meta:
        verbose_name_plural="payments"
    
    def __str__(self):
        return (self.student, self.payment_for, self.date_of_payment)
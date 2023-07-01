from django.db import models
from users.models import Student

# Create your models here.
class Payment(models.Model):
    date_of_payment=models.DateField(auto_now_add=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    payment_for=models.CharField(max_length=256)
    payment_by=models.CharField(max_length=256)
    mode_of_payment=models.CharField(max_length=256, default="Transfer")
    confirmed_by=models.CharField(max_length=256)

    class Meta:
        verbose_name_plural="payments"
    
    def __str__(self):
        return (str(self.student) + " " + self.payment_for +" received on "+ (str(self.date_of_payment)))
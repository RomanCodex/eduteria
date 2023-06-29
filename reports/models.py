from django.db import models
from users.models import Student, Teacher

# Create your models here.
class Report(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    session_id=models.CharField(max_length=9)
    subject_1=models.CharField(max_length=256)
    score_1=models.PositiveIntegerField()
    subject_2=models.CharField(max_length=256)
    score_2=models.PositiveIntegerField()
    subject_3=models.CharField(max_length=256)
    score_3=models.PositiveIntegerField()
    subject_4=models.CharField(max_length=256)
    score_4=models.PositiveIntegerField()
    subject_5=models.CharField(max_length=256)
    score_5=models.PositiveIntegerField()
    subject_6=models.CharField(max_length=256)
    score_6=models.PositiveIntegerField()
    subject_7=models.CharField(max_length=256)
    score_7=models.PositiveIntegerField()
    subject_8=models.CharField(max_length=256)
    score_8=models.PositiveIntegerField()
    subject_9=models.CharField(max_length=256)
    score_9=models.PositiveIntegerField()

    class Meta:
        verbose_name_plural="reports"
    
    def __str__(self):
        return(self.student, self.session_id)
    
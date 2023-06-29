from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=256)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=6)
    current_class=models.CharField(max_length=4)
    parent_name=models.CharField(max_length=256)
    parent_phone_number=models.CharField(max_length=14)
    address=models.CharField(max_length=256)
    genotype=models.CharField(max_length=2)
    blood_group=models.CharField(max_length=3)
    
    class Meta:
        verbose_name_plural="students"
    
    def __str__(self):
        return(self.name)

class Teacher(models.Model):
    name=models.CharField(max_length=256)
    teacher_id=models.CharField(max_length=11)
    gender=models.CharField(max_length=6)
    date_of_birth=models.DateField()
    started_work=models.DateField()
    subject=models.CharField(max_length=256)
    class_taught=models.CharField(max_length=4, blank=True)
    emergency_contact=models.CharField(max_length=256)
    emergency_contact_number=models.CharField(max_length=14)
    address=models.CharField(max_length=256)

    class Meta:
        verbose_name_plural="teachers"
    
    def __str__(self):
        return(self.name)
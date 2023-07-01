from django.shortcuts import render
from .forms import StudentForm
from reports.models import Report
from finance.models import Payment
from .models import Student, Teacher

# Create your views here.
def index(request):
    students=Student.objects.all()
    teachers=Teacher.objects.all()
    payments=Payment.objects.all()
    reports=Report.objects.all()
    context={
        "teachers":teachers,
        "students":students,
        "payments":payments,
        "reports":reports,
    }
    return render(request, "index.html", context)

def add_student(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context={
        'form':form
    }
    return render(request, 'add_student.html', context)

def student_report(request, id):
    student=Student.objects.get(id=id)
    report=Report.objects.get(student=student)
    context={
        'student':student,
        'report':report,
    }
    return render(request, 'student-details.html', context)
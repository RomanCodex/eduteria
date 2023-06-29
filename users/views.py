from django.shortcuts import render
from .forms import StudentForm
from reports.models import Report
from .models import Student

# Create your views here.
def index(request):
    return render(request, "index.html")

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
    student=Student.objects.get(id==id)
    report=Report.objects.get(student.id==id)
    context={
        'student':student,
        'report':report,
    }
    return render(request, 'student-details.html', context)
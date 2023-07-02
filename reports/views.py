from django.shortcuts import render
from .forms import ReportForm
from .models import Report

# Create your views here.
def create_report(request):
    form=ReportForm()
    if request.method=="POST":
        form=ReportForm(request.POST)
        if form.is_valid():
            form.save()
        
    context={
        'form':form
    }
    return render(request, 'create_report.html', context)

def all_reports(request):
    reports=Report.objects.all()
    context={
        "reports":reports,
    }
    return render(request, "reports.html", context)
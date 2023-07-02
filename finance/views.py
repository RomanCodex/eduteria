from django.shortcuts import render
from .models import Payment
from .forms import PaymentForm

# Create your views here.
def all_payments(request):
    payments=Payment.objects.all()
    context={
        "payments":payments
    }
    return render(request, "payments.html", context)

def add_payment(request):
    form=PaymentForm()
    if request.method=="POST":
        form=PaymentForm(request.POST)
        if form.is_valid():
            form.save()
        
    context={
        'form':form
    }
    return render(request, 'add_payment.html', context)

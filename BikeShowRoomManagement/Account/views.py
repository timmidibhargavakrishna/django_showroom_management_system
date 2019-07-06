from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import RegisterForm


def register(request):  
    return render(request, 'account/registation.html')
def add_customer(request):
    customer_id = request.POST.get('customer_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    joinng_date = request.POST.get('joining_date')
    phone_number=request.POST.get('phon_number')

    Register=RegisterForm(customer_id=customer_id,first_name=first_name,last_name=last_name,email=email,address=address,joinng_date=joinng_date,phone_number=phone_number)
    Register.save()

    return render(request,'account/registation.html')





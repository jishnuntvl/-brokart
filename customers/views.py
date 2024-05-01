from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Customer
# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            customer=Customer.objects.create(
                user=user,
                address=address,
                phone=phone
            )
            return redirect('home')
        except Exception as e:
            e_msg="dupliate u name"
            messages.error(request,e_msg)
    if request.POST and 'login' in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user )
            return redirect('home')
        else:
            e_msg="incorect u name"
            messages.error(request,e_msg)

    return render(request,'account.html')

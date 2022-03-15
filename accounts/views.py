from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        messages.error(request, 'Testing error message')
        return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        print('SUBMITTED LOGIN')
        messages.error(request, 'Testing error message')
        return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
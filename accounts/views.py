from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm
from .models import CustomerProfile
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            CustomerProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
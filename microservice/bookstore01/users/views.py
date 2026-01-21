from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from .models import Customer

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'registration/register.html')

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            Customer.objects.create(
                name=name,
                email=email,
                password=user.password,
                phoneNumber=phone_number,
                dob=dob
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Registration failed: {e}')
            return render(request, 'registration/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
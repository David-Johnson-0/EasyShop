from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'easyshopapp/home.html')

def shop(request):
    return render(request, 'easyshopapp/shop.html')

def item(request):
    return render(request, 'easyshopapp/item.html')

def checkout(request):
    return render(request, 'easyshopapp/checkout.html')

def account(request):
    return render(request, 'easyshopapp/account.html')

def settings(request):
    return render(request, 'easyshopapp/settings.html')

def login_view(request):
    return render(request, 'easyshopapp/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        credit_card = request.POST.get('credit_card')
        errors = []
        # Validation
        if not username:
            errors.append('Username is required.')
        if not email:
            errors.append('Email is required.')
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append('Invalid email address.')
        if not password or len(password) < 6:
            errors.append('Password must be at least 6 characters.')
        if not age or not age.isdigit() or int(age) < 0:
            errors.append('Valid age is required.')
        if not phone_number:
            errors.append('Phone number is required.')
        if not credit_card or len(credit_card) < 8:
            errors.append('Credit card info is required.')
        if User.objects.filter(username=username).exists():
            errors.append('Username already exists.')
        if User.objects.filter(email=email).exists():
            errors.append('Email already exists.')
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'easyshopapp/signup.html')
        user = User.objects.create(
            username=username,
            email=email,
            age=age or None,
            phone_number=phone_number,
            password=make_password(password),
            credit_card=credit_card
        )
        login(request, user)
        return redirect('home')
    return render(request, 'easyshopapp/signup.html')

def logout_view(request):
    return render(request, 'easyshopapp/logout.html')

from django.shortcuts import render

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
    return render(request, 'easyshopapp/signup.html')

def logout_view(request):
    return render(request, 'easyshopapp/logout.html')

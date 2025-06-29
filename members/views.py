from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'User with this username already exists')
            return redirect("register-user")  # ✅ Use URL name

        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()

        messages.info(request, 'User created successfully')
        return redirect("register-user")  # ✅ Use URL name

    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'User with this username does not exist')
            return redirect("login-user")  # ✅

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid password')
            return redirect("login-user")  # ✅

        login(request, user)
        messages.info(request, 'Login successful')
        return redirect('/home/polls/')

    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)
    messages.info(request, 'Logout successful')
    return redirect("login-user")  # ✅

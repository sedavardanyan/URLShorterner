from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def loginview(request):
    if request.method == "POST":
        password = request.POST['password']
        user = authenticate(request, username=request.POST["username"], password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'massage': "Wrong username or password"})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'massage': "Username already exists."})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'massage': "Passwords doesn't match."})

    else:
        return render(request, 'accounts/signup.html')


def logoutview(request):
    if User.is_authenticated:
        logout(request)
    return redirect('home')

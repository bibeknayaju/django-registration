from django.shortcuts import render, HttpResponse, redirect
# # Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('wrong')
            # return HttpResponse("Wrong username or password")
    return render(request, 'login.html')


def LogOut(request):
    logout(request)
    return redirect('login')


def Wrong(request):
    return render(request, 'wrong.html')

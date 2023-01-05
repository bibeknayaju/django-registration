from django.shortcuts import render, HttpResponse, redirect
# # Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# for contact form
from .models import Contact
# for file
from .models import FileUpload


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


# @login_required(login_url='login')
def HomePage(request):
    data = Contact.objects.all()
    file_data = FileUpload.objects.all()
    # print(data)
    if request.method == 'POST':
        contact = Contact()
        visitorname = request.POST.get('name')
        visitoremail = request.POST.get('email')
        visitorproject = request.POST.get('project')
        visitormessage = request.POST.get('message')

        contact.name = visitorname
        contact.email = visitoremail
        contact.project = visitorproject
        contact.message = visitormessage

        document = FileUpload()
        visitorfile = request.FILES['file']
        filename = visitorfile.name
        document.file = visitorfile
        # document = FileUpload.objects.create(file=visitorfile)
        document.save()

        contact.save()
        return HttpResponse("Your contact has been saved successfully")
    return render(request, 'home.html', {"data": data, "file_data": file_data})


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


def Main(request):
    return render(request, 'main.html')


def add_new_post(request):
    return render(request, 'add-new-post.html')

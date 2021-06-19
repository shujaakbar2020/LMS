from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from Management.models import *
from .forms import *
from django.contrib.auth.decorators import *


# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, usernsme=username, password=password)
            print(f'Username is {username} and Password is {password}')
            print(user)
            if user is not None:
                print('Shuja')
                login(request, user)
                return redirect('index')
        return render(request, 'Management/login.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'Management/signup.html', context)


def index(request):
    students = Student.objects.all()
    return render(request, 'Management/index.html', {'students': students})


def showStudents(request):
    students = Student.objects.all()
    return render(request, 'Management/students.html', {'students': students})


def classes(request):
    students = Student.objects.all()
    return render(request, 'Management/classes.html', {'students': students})


def dash(request):
    return render(request, 'Management/dashboard.html', {})


def grades(request):
    return render(request, 'Management/grades.html')

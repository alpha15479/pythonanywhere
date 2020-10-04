from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as logout_user
from django.contrib.auth import authenticate

def index(request):
    return render(request,'myweb/index.html')

def united(request):
    return render(request,'myweb/united.html')

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def login_active(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return render(req,'myweb/Homepage.html')

def logout(req):
    logout_user(req)
    return redirect('login')

def Homepage(request):
    return render(request,'myweb/Homepage.html')

def login_page(req):
    return render(req,'myweb/login.html')


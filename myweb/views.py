from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as logout_user
from django.contrib.auth import authenticate
from myweb.forms import MyCommentForm
from django import forms
from django.utils import timezone

def add_model(request):

    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = MyCommentForm()

        return render(request, "add.html", {'form': form})

def index(request):
    return render(request,'myweb/index.html')

def united(request):
    return render(request,'myweb/united.html')

def my_template(request):
    return render(request,'myweb/my_template.html')

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

def show_page(request):
    return render(request,'myweb/show.html')

def login_page(request):
    return render(request,'myweb/login.html')

def add_page(request):
    return render(request,'myweb/add.html')

def Vegs(request):
    return render(request,'myweb/Vegs.html')

def Fruits(request):
    return render(request,'myweb/Fruits.html')

def Pong(request):
    return render(request,'myweb/Pong.html')

def Meat(request):
    return render(request,'myweb/Meat.html')
from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")      

            newUser=User(username =username)
            newUser.set_password(password)
            newUser.save()
            loginUser(request)
            messages.info(request, "ugurla qeydiyyatdan kecdiniz")
            return redirect("index")
        context={
            "form":form
        }
        return render(request, "register.html",context)
    else:   
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request, "register.html",context)
def loginUser(requets):
    return render (requets, "login.html")
def logoutUser(request):
    logout(request)
    messages.success(request, "ugurla cixdiniz")
    return redirect("index")

def loginUser(request):
    form=LoginForm(request.POST or None)

    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "istifadeci adi ve ya parol xetalidir")
            return render(request, "login.html", context)

        messages.success(request, "ugurla daxil oldunuz")
        login(request,user)
        return redirect("index")
    return render (request, "login.html", context)

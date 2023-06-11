from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"index.html")

def plan(request):
    return render(request,"plan.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def loginView(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("index")

        else:
            messages.error(request, "Incorrect Password")

    return render(request,"login.html")

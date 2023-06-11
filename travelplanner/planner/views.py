from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url="/login")
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
        
        else:
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("index")

            else:
                messages.error(request, "Incorrect Password")

    return render(request,"login.html")

def logoutView(request):
    logout(request)
    return redirect("index")

def signup(request):
    form=UserCreationForm()

    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            user.save()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"An error occured")

    return render(request,'signup.html', {'form':form})

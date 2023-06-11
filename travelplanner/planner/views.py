from django.shortcuts import render
from django.contrib.auth import authenticate, login
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

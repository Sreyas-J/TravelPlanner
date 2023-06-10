from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def plan(request):
    return render(request,"plan.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def signup(request):
    return render(request,"signup.html")

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def plan(request):
    return render(request,"plan.html")

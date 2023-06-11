from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.index, name="index"),
    path('plan/', views.plan, name="plan"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('plan/', views.plan, name="plan"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
]
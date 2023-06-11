from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('login/', views.loginView,name="login"),
    path('plan/', views.plan,name="plan"),
    path('about/', views.plan,name="about"),
    path('contact/', views.contact, name="contact"),
]
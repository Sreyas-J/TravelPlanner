from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('login/', views.loginView,name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('plan/', views.plan,name="plan"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact, name="contact"),
]
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "register"

urlpatterns = [              
    path('register/',views.register, name="register" ),
    path('login/',views.login, name="login" ),
    path('logout/',views.logout, name="logout" ),
    path('welcome/', views.welcome, name="welcome"),
    path('updateProfile/', views.updateProfile, name="updateProfile"),
    path('registration_form_submission/', views.registration_form_submission, name='registration_form_submission'),
    path('login_form_submission/', views.login_form_submission, name='login_form_submission'),
    path('', views.index, name="index"),

]
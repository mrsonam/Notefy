
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "todolist"

urlpatterns = [
    path('tolist/', views.tolist, name="tolist"),
    path('tolist/delete/<int:pk>/', views.delete_list, name="delete_list"),
    path('cross_off/<int:pk>/', views.cross_off, name="cross_off"),
    path('uncross/<int:pk>/', views.uncross, name="uncross"),

]

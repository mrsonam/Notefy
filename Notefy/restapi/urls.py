from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gets/', views.gets, name="gets"),
    path('posts/', views.posts, name="posts"),
    path('puts/<int:pk>/', views.puts, name="puts"),
    path('deletes/<int:pk>/', views.deletes, name="deletes"),
    path('pagination/<int:PAGENO>/<int:SIZE>/', views.pagination, name="paginaton"),
]
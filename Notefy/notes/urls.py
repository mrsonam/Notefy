from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addNote/', views.addNote, name="addNote"),
    path('listNote/',views.listNote, name = "listNote"),
    path('viewNote/<int:pk>/',views.viewNote, name = "viewNote"),
    path('notePassword/<int:pk>/',views.notePassword, name = "notePassword"),
    path('note/<int:pk>/',views.delete_note, name = "delete_note"),
    path('update_note/<int:pk>/', views.update_note, name="update_note"),
]


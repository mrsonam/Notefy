from django import forms
from .models import ToDoList

class ListForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=["item", "notify_date", "completed"]
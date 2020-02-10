from django import forms
from django.contrib.auth.models import User
from .models import Profile

#form to update username and email 
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    
    class Meta:
        model= User
        fields= ['username', 'email']

#form to update profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['image']

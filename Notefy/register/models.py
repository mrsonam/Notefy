from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

# this model is used to save the profile picture of the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #OneToOneField because one user can have only one profile picture
    image = models.ImageField(default='default.jpg',upload_to='profile_pics') #default sets the profile picture of the user to default.jpg when a new user is created

    def __str__(self):
        return f'{self.user.username} Profile'
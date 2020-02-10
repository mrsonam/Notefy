from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from .forms import UserUpdateForm, ProfileUpdateForm
from todolist.models import ToDoList
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#this function renders the registration page
def register(request):       
    return render(request, "register.html")

#this function renders the welcome page
@login_required #decorator, this makes it mandatory for the user to be logged in to view the page.
def welcome(request):
    now = date.today()
    notify = ToDoList.objects.filter(user_id_id = request.user.id).all()
    return render(request, 'welcome.html', {"now": now, "notify": notify})

#this function renders the index page
def index(request):
    return render(request, 'index.html')

#this function renders the login page
def login(request):
    return render(request, 'login.html')

#this function logs out the user and redirects them to the index page
def logout(request):
    auth.logout(request)
    return redirect('/')

#this function gets the data filled by the user in the regitration page and fills the data in the database table if it is valid
def registration_form_submission(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2: #checks if password1 and password2 matches
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('register:login')

        else:   
            messages.error(request, f'Password did not match')
            return redirect('register:register')

    return render(request, "register.html")


#this function gets the username and password given by the user and checks if the user is registered or not
def login_form_submission(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('register:welcome')

    else:
        messages.error(request, f'Couldn\'t login in!! Try again ')
        return redirect('register:login')

#this function renders the update profile page 
@login_required
def updateProfile(request):
    if request.method == "POST": 
        u_form = UserUpdateForm(request.POST, instance = request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid(): #checks if the data is valid or not
            u_form.save() #saves the data into the data base
            p_form.save() #saves the data into the data base
            messages.success(request, f'Your Profile has been updated')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'updateProfile.html', context)
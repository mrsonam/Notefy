from django.shortcuts import render, redirect
from .models import Note
from django.core.files.storage import FileSystemStorage
from .forms import NoteForm
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# from .decorators import protected_note
from django.contrib import messages


# Create your views here.

# this function adds the notes as well as user key id to the respective database attributes
def addNote(request):
    if request.method == "POST":  # if the request is post
        form = NoteForm(request.POST, request.FILES)  # the entered content will be stored in the form variable
        if form.is_valid():
            instance = form.save(
                commit=False)  # form.save returns the instance and waits for not to commit and stores in the instance variable
            instance.user_id = request.user  # attaching the user_id that is logged in and grabbing the user with request.user and inserting into instance.user_id
            instance.save()  # finally saving it
            return redirect('/listNote')
    else:
        form = NoteForm()
    return render(request, 'addNote.html', {'form': form})


# the respective function list down all the created list of notes
def listNote(request):
    query = ""
    if request.GET:
        query = request.GET['q']

        note = get_data_queryset(query)
    else:
        # note = Note.objects.all()
        note = Note.objects.filter(
            user_id_id=request.user.id).all()  # storing all the object of notes as per the request by the user of respective user id in note variable

    context = {'notes': note}
    return render(request, 'listNote.html',
                  context)  # sending the stored objects to the listnote templates with key named notes to list down


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")

    for q in queries:
        notes = Note.objects.filter(

            Q(note_title__icontains=q)

        )

        for note in notes:
            queryset.append(note)

    return list(set(queryset))


def notePassword(request, pk):
    note = Note.objects.get(pk=pk)
    if note.note_password:
        if request.method == "POST":
            note_password = request.POST['current_password']
            print(note_password)
            if note.note_password == note_password:
                return render(request, 'viewNote.html', {'notes': note})

            else:
                messages.error(request, f'Wrong Password! Enter again.')
    return render(request, 'notePassword.html', {'notes': note})


# this function shows the detail view of respective note as per the key passed in its argument
def viewNote(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'viewNote.html', {'notes': note})


# this function delete the notes of the respective passed key of the note
def delete_note(request, pk):
    if request.method == "POST":  # if the request is post
        note = Note.objects.get(pk=pk)  # saves the objects of the note as per the pk in the note variable
        note.delete()  # deletes the note

    return redirect('/listNote')


# this function update the notes created
def update_note(request, pk):
    obj = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        print("success...")
        return redirect("/listNote/")
    else:
        return render(request, "update_note.html", {"form": form})


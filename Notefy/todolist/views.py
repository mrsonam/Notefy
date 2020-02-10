from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ListForm
from .models import ToDoList
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
# function to add and display lists
def tolist(request):
    query = ""
    lists = ToDoList.objects.filter(user_id_id = request.user.id).all()
    if request.GET:
        query = request.GET['q'] #gets the searched text from templates
        lists = get_data_queryset(str(query))
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid(): #check if data is valid
            instance = form.save(commit=False)  #form.save returns the instance and waits for not to commit and stores in the instance variable
            instance.user_id = request.user #attaching the user_id that is logged in and grabbing the user with request.user and inserting into instance.user_id
            instance.save() #finally saving it
            lists = ToDoList.objects.filter(user_id_id = request.user.id).all()
            messages.success(request, ('Item Has Been Added To The List :)'))
            return redirect('todolist:tolist')
        else:
            lists = ToDoList.objects.filter(user_id_id = request.user.id).all()
            messages.error(request, ('Please write something to add'))
            return redirect('todolist:tolist')
    else:
         
        return render(request, 'tolist.html', {'lists': lists}) #renders the todolist page

# function to delete lists using slug
def delete_list(request, pk):
     item = ToDoList.objects.get(pk=pk)  
     item.delete()
     messages.success(request, ('Item Has Been Deleted'))
     return redirect('todolist:tolist')

# function to change the status of the list as completed
def cross_off(request, pk):
    item = ToDoList.objects.get(pk=pk)
    item.completed=True
    item.save()
    return redirect('todolist:tolist')

# function to change the status of the list as incomplete
def uncross(request, pk):
    item = ToDoList.objects.get(pk=pk)
    item.completed=False
    item.save()
    return redirect('todolist:tolist')

# function to search lists
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        lists = ToDoList.objects.filter(
            Q(item__icontains=q)

        )

        for l in lists:
            queryset.append(l)
    return list(set(queryset))


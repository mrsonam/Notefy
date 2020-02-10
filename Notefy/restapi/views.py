from django.shortcuts import render
from .models import ApiModel
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def gets(request):
    if request.method == "GET":
        user = ApiModel.objects.all()
        dict_user = {"user": list(user.values("user_name","user_address","user_contact"))}
        return JsonResponse(dict_user)
    else:
        return JsonResponse({"Error":"Not Allowed"})
        
@csrf_exempt
def puts(request, pk):
    user = ApiModel.objects.get(pk=pk)
    
    if request.method == "PUT":
        decoded_user = request.body.decode('utf-8')
        data = json.loads(decoded_user)
        user.user_name = data['user_name']
        user.user_address = data['user_address']
        user.user_contact = data['user_contact']
        user.save()
        return JsonResponse({"message": "Completed Successfully!!"})
    
    return JsonResponse({"Error":"Not Allowed"})

def getbyid(request, pk):
    user = ApiModel.objects.get(pk=pk)

    if request.method == "GET":
        return JsonResponse({"user_name": user.user_name, "user_address": user.user_address, "user_contact": user.user_contact})

    return JsonResponse({"Error":"Not Allowed"})

@csrf_exempt
def posts(request):
    if request.method == "POST":
        decoded_user = request.body.decode('utf-8')
        data = json.loads(decoded_user)
        user_name = data['user_name']
        user_address = data['user_address']
        user_contact = data['user_contact']
        ApiModel.objects.create(user_name=user_name,user_address=user_address,user_contact=user_contact)
        return JsonResponse({"message": "Completed Successfully!!"})
    
    return JsonResponse({"Error":"Not Allowed"})

def pagination(request, PAGENO, SIZE):
    skip= SIZE * (PAGENO-1)
    user = ApiModel.objects.all() [skip:(PAGENO * SIZE)]
    dict= {
            "user": list(user.values("user_name"))
    }
    return JsonResponse(dict)

@csrf_exempt
def deletes(request, pk):
    user = ApiModel.objects.get(pk=pk)
    if request.method == "DELETE":
        user.delete()
        return JsonResponse({"message": "Completed Successfully!!"})
    
    else:
        return JsonResponse({"message": "Error!!"})

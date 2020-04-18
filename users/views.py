from django.shortcuts import render
import os
import datetime
from django.http import HttpRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login, logout
from .models import customer, store, User, store_info, store_news
from django.utils.datastructures import MultiValueDictKeyError
from django.db.utils import IntegrityError
import json
from django.views.decorators.csrf import csrf_exempt
# from django.conf.urls.defaults import *


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = (request.body.decode())
        print(type(data))
        data = eval(data)
        username = data['username']
        password = data['passwd']
        # user = User.objects.filter(username=username).first()
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        mycustomer = customer()
        mycustomer.user = user
        mycustomer.save()
        return JsonResponse({
            "status": "success",
            "type" : "user",
            'username' : username
        })

    # pass


@csrf_exempt
def signin(request):
    data = (request.body.decode())
    data = eval(data)
    username = data['username']
    password = data['passwd']  
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({
            'status': 'fail' ,
            'type' : 'user'
        })
    login(request, user)
    mycustomer = customer.objects.filter(user=user).first()
    if mycustomer is None :
        return JsonResponse({
            'status': 'success' ,
            'type' : 'store',
            'username' : username
        })
    else :
        return JsonResponse({
            'status': 'success' ,
            'type' : 'user',
            'username' : username
        })
    pass

@csrf_exempt
def update(request):
    data = (request.body.decode())
    data = eval(data)
    username = data['username']
    name_person = data['name']
    get_cus = customer.objects.get(user__username = username)
    get_cus.name = name_person
    get_cus.save()
    final = {
        'status' : 'success',
    }
    return JsonResponse(final) 


@csrf_exempt
def restaurant(request):
    all_res = list(store.objects.filter(category = 'restaurant').values("user__username"))
    return JsonResponse({"items" : all_res})

@csrf_exempt
def shops(request):
    all_res = list(store.objects.filter(category = 'shops').values("user__username"))
    return JsonResponse({"items" : all_res})

@csrf_exempt
def clinic(request):
    all_res = list(store.objects.filter(category = 'clinic').values("user__username"))
    return JsonResponse({"items" : all_res})


@csrf_exempt
def getstoreinfo(request):
    data = (request.body.decode())
    data = eval(data)
    username = data['username']
    # name_person = data['name']
    info = list(store_info.objects.filter(store_id__user__username = username).values("location" , "count"))
    return JsonResponse({"info" : info})

@csrf_exempt
def getstorenews(request):
    info = list(store_news.objects.filter().order_by('-time_of_post').values("news"))
    return JsonResponse({"info" : info})



from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import *
# Create your views here.
import mp_app.util.CommonUtil as util

def index(request):
    return HttpResponse('Hello World, This is Home Page. ' + str(util.current_timestamp()))
    
def getUserInfoByUserId(request, userId):
    try:
        result = User.objects.get(id=userId).toJSON()
        return util.json_encode(result)
    except:
        return util.json_encode_errorMsg("User Not Found")

def getAllMusic(request):
    try:
        results = Music.objects.all().values('id', 'name', 'user')
        return util.json_encode(list(results))
    except:
        return util.json_encode_errorMsg("Music Not Found")
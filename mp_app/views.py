from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import *
# Create your views here.
import mp_app.util.CommonUtil as util

config = {
    'encoding': 'utf-8'
}

def index(request):
    return HttpResponse('Hello World, This is Home Page. ' + str(util.current_timestamp()))
    
def getUserInfoByUserId(request, userId):
    try:
        result = User.objects.get(id=userId).toJSON()
        return util.json_encode(result, True)
    except:
        return util.json_encode("User Not Found", False)

def getAllMusic(request):
    try:
        results = Music.objects.all().values('id', 'name', 'user')
        return util.json_encode(list(results), True)
    except:
        return util.json_encode("Music Not Found", False)

def searchMusic(request):
    request.encoding=config['encoding']
    if 'q' in request.GET:
        keyword = request.GET['q']
        result = Music.objects.filter(name__icontains=keyword).values('id', 'name', 'user')
        if len(result) > 0:
            return util.json_encode(list(result), True)
        else:
            return util.json_encode('not found', False)
    else:
        return util.json_encode('keyword is null', False)

def register(request):
    request.encoding=config['encoding']
    return util.json_encode(request.POST, True)
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
# Create your views here.

# test http request
def testHttp(request):
    return HttpResponse('test Request')
# test json request
def testJson(request):
    return JsonResponse({'debug':'json mode2'})
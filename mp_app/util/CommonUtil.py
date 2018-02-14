import json
from django.http import JsonResponse

def current_timestamp():
    import calendar;
    import time;
    ts = calendar.timegm(time.gmtime())
    return ts

def json_encode(data):
    response = {
        "success": True,
        "server_time": current_timestamp(),
        "response": data,
    }
    return JsonResponse(response, safe=False)
 
def json_encode_errorMsg(msg):
    response = {
        "success": False,
        "server_time": current_timestamp(),
        "error_msg": msg,
    }
    return JsonResponse(response, safe=False)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import json

import environ
env = environ.Env()

# Create your views here.

def index(request):
    return HttpResponse("Hi")

def test(request):
    return HttpResponse("OK")

@require_http_methods(["GET"])
def check_env(request):
    environment = env("_ENV", default="staging")
    return HttpResponse(environment)

@csrf_exempt
@require_http_methods(["POST"])
def callout(request):
    pure_body = request.body
    try:
        body = json.loads(pure_body)
        num = int(body['num'])
    except ValueError as e:
        return HttpResponse("Error parsing body: " + str(e))
    except Exception as e:
        return HttpResponse("Error parsing body: " + str(e))
    
    results = cal_impower(num)

    res = {
        "results": results
    }

    return JsonResponse(res)

def cal_impower(num):
    results = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append('IM IMPOWER')
        elif i % 3 == 0:
            results.append('IM')
        elif i % 5 == 0:
            results.append('IMPOWER')
        else:
            results.append(str(i))
    return results

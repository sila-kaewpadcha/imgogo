from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import json

import environ
env = environ.Env()

# Create your views here.

def index(request):
    return HttpResponse("Hi")

def test(request):
    return HttpResponse("OK new env 99")

@require_http_methods(["GET"])
def check_env(request):
    environment = env("_ENV", default="staging")
    print('hi environment: ', environment)
    return HttpResponse('hi env: ' + environment)

@csrf_exempt
@require_http_methods(["POST"])
def callout(request):
    print('hi callout')
    return HttpResponse("Hi Callout POST API")

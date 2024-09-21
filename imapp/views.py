from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return HttpResponse("Hi")

def test(request):
    return HttpResponse("OK new env last test 44")

def check_env(request):
    return HttpResponse("Check ENV")

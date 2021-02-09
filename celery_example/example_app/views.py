from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, add

# Create your views here.

def index(request):
    sleepy.delay(10)
    return HttpResponse("Done!!!")

def add_nums(request):
    add.delay(10,20)
    return HttpResponse("Added Done!!!")
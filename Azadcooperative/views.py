# I have created this -prince
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to the main project page")

def about(request):
    return HttpResponse("About")
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hello")

def members(request):
    return HttpResponse(f"categories")

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.

def home_view(request):
    return JsonResponse({"Home": 1})

def about_view(request):
    return JsonResponse({"About": 2})

def contact_view(request):
    return JsonResponse({"Contact": 3})
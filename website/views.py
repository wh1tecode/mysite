from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.

def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return JsonResponse({"About": 2})

def contact_view(request):
    return JsonResponse({"Contact": 3})
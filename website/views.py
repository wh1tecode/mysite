from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.

def home_view(request):
    context = {
        "twitter": "https://www.x.com/", 
        "facebook": "https://facebook.com", 
        "instagram": "https://www.instagram.com",
        "skype": "https://www.skype.com/",
        "linkedin": "https://www.linkedin.com/",
    }
    return render(request=request, template_name="index.html",context=context)
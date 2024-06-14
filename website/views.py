from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from website.models import About, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm


# Create your views here.

# @login_required(login_url="/")
def home_view(request, page_id):
    context = {
        "social_media": {
            "twitter": "https://www.x.com/",
            "facebook": "https://facebook.com",
            "instagram": "https://www.instagram.com",
            "skype": "https://www.skype.com/",
            "linkedin": "https://www.linkedin.com/",
        }
    }
    try:
        user = User.objects.get(id=page_id)
        return render(request=request, template_name="resume\index.html", context=context)
    except Exception:
        return redirect("/")



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home/")
    else:
        form = LoginForm()
    return render(
        request=request, template_name="login\index.html", context={"form": form}
    )


def logout_view(request):
    return


def create_resume_view(request):
    return render(
        request=request, template_name="create_resume\index.html"
    )

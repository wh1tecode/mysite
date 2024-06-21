from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from website.models import About, User, Skill
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm, CompleteUserData
from django.contrib.auth.models import User as AdminUser
from django.contrib.auth.hashers import make_password
from website.utils import set_user_permissions_to_admin


# Create your views here.


@login_required(login_url="/")
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
    user = User.objects.get(url_address=page_id)
    return render(request=request, template_name="resume\index.html", context=context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                admin = AdminUser.objects.get(username=username)
                user = User.objects.get(admin=admin)
                return redirect("/home/" + user.url_address)
    else:
        form = LoginForm()
    return render(
        request=request, template_name="login\index.html", context={"form": form}
    )


def logout_view(request):
    return


def complete_user_data(request):

    if request.method == "POST":
        form = CompleteUserData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            auth = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if auth:
                return redirect("/create_resume")
            admin = AdminUser()
            admin.username = form.cleaned_data["username"]
            admin.password = make_password(form.cleaned_data["password"])
            admin.is_active = True
            admin.is_staff = True
            admin.is_superuser = False
            user = User()
            user.admin = admin
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.phone_number = form.cleaned_data["phone_number"]
            user.email_address = form.cleaned_data["email_address"]
            user.birth_date = form.cleaned_data["birth_date"]
            user.avatar_image = form.cleaned_data["avatar_image"]
            about = About()
            about.title = form.cleaned_data["about_title"]
            about.description = form.cleaned_data["about_description"]
            about.website = form.cleaned_data["about_website"]
            about.city = form.cleaned_data["about_city"]
            about.degree = form.cleaned_data["about_degree"]
            about.freelance = form.cleaned_data["about_is_freelancer"]
            about.owner = user
            admin.save()
            set_user_permissions_to_admin(
                admin,
                [
                    "add_about",
                    "delete_about",
                    "add_user",
                    "delete_user",
                ],
            )
            auth = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            login(request, auth)
            user.save()
            about.save()
            for s in form.cleaned_data:
                if "skill" in s:
                    skill = Skill()
                    skill.about = about
                    skill.name = s
                    skill.score = form.cleaned_data[s]
                    skill.save()
            return redirect("/home/" + user.url_address)

    return HttpResponse(content={})


def create_resume_view(request):
    skills = {"python": 0, "django": 0, "linux": 0, "javascript": 0}
    context = {"skills": skills}

    return render(
        request=request, template_name="create_resume\index.html", context=context
    )

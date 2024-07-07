from time import sleep
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from website.models import About, User, Education, Experience, Project, Skill, Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm, CompleteUserData, ContactUs
from django.contrib.auth.models import User as AdminUser
from django.contrib.auth.hashers import make_password
from website.utils import set_user_permissions_to_admin, calculate_age
from django.contrib.messages import get_messages
from django.contrib import messages
from datetime import datetime
from os.path import join


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
    user = User.objects.get(url_address=page_id)
    about = About.objects.get(owner=user)
    education = Education.objects.filter(owner=user)
    experience = Experience.objects.filter(owner=user)
    project = Project.objects.filter(owner=user)
    skill = Skill.objects.filter(about=about)

    context["user_projects"] = [x.__dict__ for x in project]
    context["user_projects_name"] = [x["name"] for x in context["user_projects"]]
    context["user_first_name"] = user.first_name
    context["user_last_name"] = user.last_name
    context["user_birthday"] = user.birth_date.strftime("%m/%d/%Y")
    context["user_avatar_image"] = user.avatar_image
    context["user_banner_image"] = user.banner_image
    context["user_age"] = user.age
    context["user_phone_number"] = user.phone_number
    context["user_email_address"] = user.email_address
    context["user_title"] = about.title
    context["user_description"] = about.description
    context["user_website"] = about.website
    context["user_city"] = about.city
    context["user_degree"] = about.degree
    context["user_is_freelance"] = "Available" if about.freelance else "Unavailable"
    context["user_education"] = [x.__dict__ for x in education]
    context["user_experience"] = [x.__dict__ for x in experience]
    context["user_project"] = [x.__dict__ for x in project]
    context["user_skills"] = [x.__dict__ for x in skill]
    for user_education in context["user_education"]:
        user_education["started_date"] = user_education["started_date"].strftime("%Y")
        user_education["ended_date"] = user_education["ended_date"].strftime("%Y")
    for user_experience in context["user_experience"]:
        user_experience["responsibilities"] = [
            x for x in user_experience["responsibilities"].split("\r\n") if x
        ]
        user_experience["started_date"] = user_experience["started_date"].strftime("%Y")
        user_experience["ended_date"] = user_experience["ended_date"].strftime("%Y")
    return render(
        request=request, template_name=join("resume", "index.html"), context=context
    )


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
        request=request,
        template_name=join("login", "index.html"),
        context={"form": form},
    )


def logout_view(request):
    return


def complete_user_contact_us(request):
    print(request.headers)
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data["name"]
            contact.email = form.cleaned_data["email"]
            contact.subject = form.cleaned_data["subject"]
            contact.message = form.cleaned_data["message"]
            url_address = request.headers.get("Referer").split("/")[-1]
            user = User.objects.get(url_address=url_address)
            contact.owner = user
            contact.save()
            return redirect(request.headers.get("Referer"))

    return HttpResponse(content={})


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
                messages.add_message(
                    request=request,
                    level=messages.ERROR,
                    message="username already exists",
                )
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
            user.age = calculate_age(user.birth_date)
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
            print("save admin")
            set_user_permissions_to_admin(
                admin,
                [
                    "add_about",
                    "delete_about",
                    "add_user",
                    "delete_user",
                    "add_contact",
                    "change_contact",
                ],
            )
            print("set_user_permissions_to_admin")
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
                    skill.name = s.split("skill_")[-1]
                    skill.score = form.cleaned_data[s]
                    skill.save()
            return redirect("/home/" + user.url_address)
        else:
            for msg in form.errors.get_json_data(True):
                msg = msg.replace("_", "").upper()
                messages.warning(
                    request=request, message=f"this field is required {msg}"
                )
            return redirect("/create_resume")
    return HttpResponse(content={})


def create_resume_view(request):
    skills = {"python": 0, "django": 0, "linux": 0, "javascript": 0}
    context = {"skills": skills}

    return render(
        request=request,
        template_name=join("create_resume", "index.html"),
        context=context,
    )

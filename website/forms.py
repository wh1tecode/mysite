from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CompleteUserData(forms.Form):
    avatar_image = forms.FileField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(required=False)
    birth_date = forms.DateField()
    email_address = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    about_title = forms.CharField()
    about_website = forms.URLField(required=False)
    about_city = forms.CharField()
    about_degree = forms.CharField()
    about_is_freelancer = forms.BooleanField()
    about_description = forms.CharField(required=False)
    skill_python = forms.IntegerField(required=False)
    skill_django = forms.IntegerField(required=False)
    skill_linux = forms.IntegerField(required=False)
    skill_javascript = forms.IntegerField(required=False)

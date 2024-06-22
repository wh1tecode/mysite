from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User as AdminUser
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    url_address = models.CharField(max_length=32, default=str(uuid4().hex))
    birth_date = models.DateField()
    avatar_image = models.ImageField(default=None)
    banner_image = models.ImageField(default=None)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    admin = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    class meta:
        ordering = "created_date"
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class About(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    website = models.URLField(blank=True)
    city = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    freelance = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    about = models.ForeignKey(About, on_delete=models.CASCADE)



class Education(models.Model):
    title = models.CharField(max_length=30)
    institution = models.CharField(max_length=30, default=None)
    degree = models.CharField(max_length=30, default=None)
    gpa = models.FloatField()
    started_date = models.DateField(auto_now_add=True)
    ended_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Experience(models.Model):
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30, default=None)
    responsibilities = models.JSONField()
    started_date = models.DateField(auto_now_add=True)
    ended_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(blank=True)
    description = models.TextField()
    repository = models.CharField(max_length=50, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Portfolio(models.Model):
    name = models.CharField(max_length=30, default=None)
    repository = models.CharField(max_length=50, default=None)
    image = models.BinaryField()
    url = models.URLField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True)

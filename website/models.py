from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=50)
    birth_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class meta:
        ordering = "created_date"


class About(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    website = models.URLField(blank=True)
    city = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    freelance = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    about = models.ForeignKey(About, on_delete=models.CASCADE)


class Resume(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()


class Education(models.Model):
    title = models.CharField(max_length=30)
    gpa = models.FloatField()
    grade = models.CharField(max_length=30, default=None)
    image = models.BinaryField(default=None)
    description = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Experience(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    score = models.IntegerField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Portfolio(models.Model):
    image = models.BinaryField()
    link = models.URLField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=30)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True)

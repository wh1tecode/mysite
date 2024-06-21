from django.contrib import admin
from website.models import *


# Register your models here.



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "email_address",
        "url_address",
        "birth_date",
    )
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user.id)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "title",
        "website",
        "city",
        "degree",
        "freelance",
    )
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.id)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "score",
    )
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(about=request.user.id)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.id)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.id)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.id)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user.id)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("name", "email", "created_date")
    list_filter = ("email",)
    search_fields = ("name", "message")

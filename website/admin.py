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
        "birth_date",
    )


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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("name", "email", "created_date")
    list_filter = ("email",)
    search_fields = ("name", "message")

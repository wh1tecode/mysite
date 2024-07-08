from django.contrib import admin
from django.contrib.auth.models import User as AdminUser
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

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            print(request.user.is_superuser)
            return super(UserAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        user = AdminUser.objects.get(id=request.user.id)
        context["adminform"].form.fields["admin"].queryset = AdminUser.objects.filter(
            id=user.id
        )

        return super(UserAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = AdminUser.objects.get(id=request.user.id)
        return qs.filter(admin=user)


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

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super(AboutAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        user = AdminUser.objects.get(id=request.user.id)
        context["adminform"].form.fields["owner"].queryset = User.objects.filter(
            admin=user
        )

        return super(AboutAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        return qs.filter(owner=user)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "score",
    )

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super(SkillAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        about = About.objects.get(owner=user)

        context["adminform"].form.fields["about"].queryset = About.objects.filter(
            owner=user
        )

        return super(SkillAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        about = About.objects.get(owner=user)
        return qs.filter(about=about)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super(EducationAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        user = AdminUser.objects.get(id=request.user.id)
        context["adminform"].form.fields["owner"].queryset = User.objects.filter(
            admin=user
        )

        return super(EducationAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        return qs.filter(owner=user)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super(ExperienceAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        user = AdminUser.objects.get(id=request.user.id)
        context["adminform"].form.fields["owner"].queryset = User.objects.filter(
            admin=user
        )

        return super(ExperienceAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        return qs.filter(owner=user)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProjectAdmin, self).render_change_form(
                request, context, *args, **kwargs
            )
        user = AdminUser.objects.get(id=request.user.id)
        context["adminform"].form.fields["owner"].queryset = User.objects.filter(
            admin=user
        )

        return super(ProjectAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        return qs.filter(owner=user)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "message",
    )
    
    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        auser = AdminUser.objects.get(id=request.user.id)
        user = User.objects.get(admin=auser)
        return qs.filter(owner=user)

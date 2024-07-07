from website.models import About, User, Skill, Education, Experience, Project, Contact
from django.contrib.auth.models import User as AdminUser, Permission
from django.contrib.contenttypes.models import ContentType
from typing import Optional
from datetime import date


def set_user_permissions_to_admin(
    admin: AdminUser,
    skip_permissions_list: Optional[list[str]] = None,
    add_permissions_list: Optional[list[str]] = [],
) -> list[Permission]:
    list_of_permissions = []
    user_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(User)
    )
    print(user_permission)
    about_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(About)
    )
    print(about_permission)
    education_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Education)
    )
    experience_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Experience)
    )
    project_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Project)
    )
    skill_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Skill)
    )
    contact_permission = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Contact)
    )
    list_of_permissions += user_permission
    list_of_permissions += about_permission
    list_of_permissions += education_permission
    list_of_permissions += experience_permission
    list_of_permissions += project_permission
    list_of_permissions += skill_permission
    list_of_permissions += contact_permission
    if skip_permissions_list:
        list_of_permissions = [
            perm
            for perm in list_of_permissions
            if perm.codename not in skip_permissions_list
        ]
    for permission in list_of_permissions:
        print(permission.codename)
        admin.user_permissions.add(permission)

    for permission in add_permissions_list:
        print(permission)
        admin.user_permissions.add(permission)
    return list_of_permissions

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
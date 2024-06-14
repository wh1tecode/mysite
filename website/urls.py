from django.urls import path
from website.views import home_view, create_resume_view, login_view


urlpatterns = [
    path('', login_view),
    path('home/<str:page_id>', home_view),
    path('create_resume/', create_resume_view)
]

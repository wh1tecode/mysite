from django.urls import path
from website.views import home_view, login_view


urlpatterns = [
    path('', login_view),
    path('home/', home_view)
]

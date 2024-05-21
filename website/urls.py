from django.urls import path
from website.views import home_view


urlpatterns = [
    path('', home_view),
]

from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.user_login, name="user_login"),
    path("sign-out/", views.user_logout, name="user_logout"),
    path("profile/", views.user_profile, name="user_profile"),
    path("register/", views.user_register, name="user_register"),
]

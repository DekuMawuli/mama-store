from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .decor import unauthenticated_user
from shop.decors import authenticated_user

# Create your views here.


@unauthenticated_user
def user_login(request):
    pass


@authenticated_user
def user_logout(request):
    pass


@authenticated_user
def user_register(request):
    pass


@authenticated_user
def user_profile(request):
    pass

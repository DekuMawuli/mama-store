from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You Are Already Logged In")
            return redirect("shop:home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

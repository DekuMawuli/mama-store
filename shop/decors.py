from django.shortcuts import redirect
from django.contrib import messages


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.info(request, "You Are Already Logged In")
            return redirect("users:user_login")
    return wrapper_func

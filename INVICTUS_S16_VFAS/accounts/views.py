from django.shortcuts import redirect, render
from django.contrib.auth import models
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def register(request):
    template_name = "accounts/register.html"
    if request.user.is_authenticated:
        return redirect("events:dashboard")

    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        context = {}
        try:
            user = models.User.objects.get(username=username)
            context["message"] = "Account already exists"
            context["type"] = "danger"
        except:
            if username[-10:] != "@ves.ac.in":
                context["message"] = "Not a ves email id!"
                context["type"] = "warning"
            else:
                user = models.User(username=username, email=username)
                user.set_password(password)
                user.save()
                auth_login(request, user)

                return redirect("events:dashboard")
        return render(request, template_name, context)

    return render(request, template_name)


def login(request):
    template_name = "accounts/login.html"
    if request.user.is_authenticated:
        return redirect("events:dashboard")
    context = {}
    if request.method == "POST":
        user = authenticate(
            request, username=request.POST["email"], password=request.POST["password"]
        )
        if user:
            auth_login(request, user)
            return redirect("events:dashboard")
        context["message"] = "Invalid Crediantials"
        context["type"] = "danger"
    return render(request, template_name, context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

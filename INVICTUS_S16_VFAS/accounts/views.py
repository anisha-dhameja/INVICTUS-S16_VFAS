from re import template
from django.shortcuts import render
from accounts import models
from django.contrib import messages


def register(request):
    template_name = "accounts/register.html"
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = models.User.objects.get(email)
        if user is not None:
            # already exists
            messages.error(request, 'Account already exists')
            pass
        else:
            u = models.User()
            u.email = email
            u.set_password(password)
            u.save()
            messages.success(request, 'Account created successfully!')
            return render(request, 'account/dashboard.html')
    return render(request, template_name)


def login(request):
    template_name = "accounts/login.html"
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = models.User.objects.get(email)
        if user is not None:
            if user.check_password(password):
                return render(request, 'accounts/dashboard.html')
            else:
                messages.error(request, 'Invalid credentials!')
        else:
            messages.error(request, 'Invalid credentials!')
    return render(request, template_name)

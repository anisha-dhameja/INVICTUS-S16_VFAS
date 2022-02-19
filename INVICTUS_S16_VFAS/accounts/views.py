from re import template
from django.shortcuts import render


def register(request):
    template_name = "accounts/register.html"
    return render(request, template_name)


def login(request):
    template_name = "accounts/login.html"
    return render(request, template_name)

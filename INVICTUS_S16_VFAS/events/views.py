from django.shortcuts import render


def dashboard(request):
    return render(request, "events/dashboard.html")
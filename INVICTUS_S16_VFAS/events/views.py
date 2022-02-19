from django.shortcuts import render


def dashboard(request):
    return render(request, "events/dashboard.html", context={"lst": range(10)})


def details(request):
    return render(request, 'events/details.html', context={'students': range(10)})
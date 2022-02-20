from django.shortcuts import render
from events import models as event_models


def dashboard(request):
    events = event_models.Event.objects.all()
    user = request.user
    button_text="" 
    if user.is_superuser:
        button_text= "Details"
    else:
        button_text = "Register"
    return render(request, "events/dashboard.html", context={"events":events,"details":button_text})


def details(request, slug):
    event = event_models.Event.objects.filter(slug=slug).first()
    return render(request, 'events/details.html', context={'event': event})

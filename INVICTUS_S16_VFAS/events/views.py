from django.shortcuts import render,redirect
from events import models as event_models
from django.utils.text import slugify

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
    events = event_models.Event.objects.all()
    print(events)
    for e in events.objects.definitions.all():
        ename = slugify(e.event_name)
        if ename == slug:
            event = e
            break
    # return render('event:details', event_name=event.slug)
    return render(request, 'events/details.html', context={'students': event.users})
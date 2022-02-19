from asyncio import events
from re import T
from django.db import models
from django.contrib.auth import models as auth_models
from feedbacks import models as feedback_models
from events import models as events_models

# Create your models here.


class User(auth_models.AbstractUser):
    email = models.EmailField(max_length=300, unique=True)
    USERNAME_FIELD = "email"
    username = None
    questions = models.ManyToManyField(
        feedback_models.FeedbackQuestions)
    events = models.ManyToManyField(events_models.Events)
    branch = models.CharField(max_length=200)

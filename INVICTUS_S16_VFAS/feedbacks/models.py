from django.db import models
from events import event_models
from accounts import user_models
# Create your models here
class FeedBackQuestions(models.Model):
    questions = models.CharField(max_length=100)
    events = models.ForeignKey(event_models.Events, on_delete=models.CASCADE, related_name="questions")
    

class FeedBackResponse(models.Model):
    user = models.ManyToManyField(user_models.User, on_delete=models.CASCADE, related_name="user")
    questions = models.ForeignKey(FeedBackQuestions, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)
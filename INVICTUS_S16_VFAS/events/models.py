from django.db import models
class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    first_year = models.BooleanField()
    second_year = models.BooleanField()
    third_year = models.BooleanField()
    fourth_year = models.BooleanField()
# Create your models here.

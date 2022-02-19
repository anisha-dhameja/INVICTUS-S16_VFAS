from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    slug = models.SlugField(default="", editable=False, max_length=500, unique=True)
    event_name = models.CharField(max_length=256)
    event_date = models.DateField()
    event_time = models.TimeField()
    first_year = models.BooleanField()
    second_year = models.BooleanField()
    third_year = models.BooleanField()
    fourth_year = models.BooleanField()
    upload_image = models.ImageField(upload_to="uploads/")

    def save(self, *args, **kwargs):
        value = slugify(self.event_name)
        self.slug = value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.event_name


from django.contrib.auth import models as auth_models
from django.db import models


class User(auth_models.AbstractUser):
    year = models.CharField(max_length=10)
    division = models.CharField(max_length=10)

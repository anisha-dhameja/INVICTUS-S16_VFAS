from django.contrib import admin
from accounts import models as auth_models

admin.site.register(auth_models.User)
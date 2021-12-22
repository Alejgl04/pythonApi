from django.contrib import admin
from django.db import models
from profiles_api import models

admin.site.register(models.UserProfile)
# Register your models here.

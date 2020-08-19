from django.contrib import admin

from fprofiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
# Register your models here.

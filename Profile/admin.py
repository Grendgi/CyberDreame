from django.contrib import admin
from .models import UserProfile, GameProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(GameProfile)

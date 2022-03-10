from django.contrib import admin
from users.models import CatPhotos
from users.models import UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CatPhotos)


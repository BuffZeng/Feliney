from django.contrib import admin
from users.models import Catimessage
from users.models import CatRatings
from users.models import CatPhotos
from users.models import UserProfile
from users.models import Catmessage
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CatPhotos)
admin.site.register(CatRatings)
admin.site.register(Catmessage)
admin.site.register(Catimessage)


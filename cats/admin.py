from django.contrib import admin
from cats.models import CatProfile, CommentTable

# Register your models here.
admin.site.register(CatProfile)
admin.site.register(CommentTable)


from django.contrib import admin
from cats.models import CatProfile, CommentTable

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('breed',)}
admin.site.register(CatProfile, CatAdmin)
admin.site.register(CommentTable)


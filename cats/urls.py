from unicodedata import name
from django.urls import path
from cats import views
app_name = 'cats'
urlpatterns = [
    path('', views.cat_profile, name='cat_profile'),
]
from unicodedata import name
from django.urls import path
from cats import views
app_name = 'cats'
urlpatterns = [
    path('search/',views.search, name='search'),
    path('<slug:cat_name_slug>/',views.show_cat, name='show_cat'),
]
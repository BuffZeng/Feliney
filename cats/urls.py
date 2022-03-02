from django.urls import path
from cats import views
app_name = 'rango'
urlpatterns = [
    path('', views.cat_profile, name='cat_profile'),
]
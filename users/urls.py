from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
path('',views.index, name='index'),
path('personal_info/',views.personal_info,name='personal_info'),
path('edit_ratings/',views.edit_ratings,name='edit_ratings'),
path('all_coments/',views.all_coments, name='all_coments'),
path('upload_image/',views.upload_image,name='upload_image'),
path('login/',views.login,name='login'),
path('home/',views.home_page,name='home_page'),
path('edit/',views.edit_user,name='edit_user'),
path('add_cat/',views.add_cat,name='add_cat'),
path('logout/',views.user_logout,name='user_logout')
]
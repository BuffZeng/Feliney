from django.urls import path
from users.views import draftnew
from users import views

app_name = 'users'

urlpatterns = [
path('',views.index, name='index'),
path('personal_info/',views.personal_info,name='personal_info'),
path('edit_ratings/',views.edit_ratings,name='edit_ratings'),
path('all_coments/',views.all_coments, name='all_coments'),
path('upload_image/',views.upload_image,name='upload_image'),
path('register/',views.register,name='register'),
path('login/',views.login,name='login'),
path('home/',views.home_page,name='home_page'),
path('edit/',views.edit_user,name='edit_user'),
path('add_cat/',views.add_cat,name='add_cat'),
path('logout/',views.user_logout,name='user_logout'),
path('pre_cat_ratings/',views.pre_cat_ratings,name='pre_cat_ratings'),
path('messaging/',views.messaging,name='messaging'),
path('new_message/',views.new_message,name='new_message'),
path('draft_new/',views.draftnew,name='draftnew')
]
# from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns=[
   re_path('^$',views.post,name='post'),
   re_path(r'^register/', views.register, name='register'),
   re_path(r'^login/', views.login_page, name='login'),
   re_path(r'^logout/', views.logoutUser, name="logout"),
   re_path('profile/<username>/', views.profile, name='profile'),
   re_path('user_profile/<username>/', views.user_profile, name='user_profile'),
   re_path(r'^image/(\d+)',views.image,name ='image'),





]
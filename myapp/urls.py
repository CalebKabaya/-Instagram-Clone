# from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns=[
   re_path('^$',views.welcome,name='welcome'),
   re_path(r'^register/', views.register, name='register'),
   re_path(r'^login/', views.login_page, name='login'),
   re_path(r'^logout/', views.logoutUser, name="logout"),




]
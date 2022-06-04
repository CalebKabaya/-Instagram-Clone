# from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns=[
   re_path('^$',views.welcome,name='welcome'),
   re_path('register/', views.register, name='register'),
   re_path('login/', views.login, name='login'),
   re_path('logout/', views.logoutUser, name="logout"),


]
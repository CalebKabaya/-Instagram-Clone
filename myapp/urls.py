# from django.conf.urls import url
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns=[
   re_path('^$',views.post,name='post'),
   re_path(r'^register/', views.register, name='register'),
   re_path(r'^login/', views.login_page, name='login'),
   re_path(r'^logout/', views.logoutUser, name="logout"),
   # re_path('profile/<username>/', views.profile, name='profile'),
   # re_path('profile/<username>/', views.profile, name='profile'),

   # re_path('user_profile/<username>/', views.user_profile, name='user_profile'),
   re_path(r'^image/(\d+)',views.image,name ='image'),
   # re_path(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
   re_path(r'^search/', views.search_results, name='search_results'),
   # re_path('profile/<username>/', views.profile, name='profile'),
   re_path('user_profile/<username>/', views.user_profile, name='user_profile'),
   re_path('profile/', views.profile, name='profile'),
   # re_path(r'^<int:post_id>/like',views.like, name = 'postlike'),
   re_path(r'^like/(?P<image_id>\d+)',views.like, name = 'postlike'),
   re_path('comments/<int:pk>' , views.new_comment, name='comment'),
   re_path(r'^comments/(?P<pk>\d+)' , views.new_comment, name='comment'),







  
    








]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'userpage'
urlpatterns = [
    path('', homepage, name='home'),
    path('post', post, name='post'),
    path('<int:postId>', delPost, name='del'),
    path('<str:username>',userProfile,name='userprofile'),
    path('like/<int:postId>', LikePost, name='like'),
    path('slug/comment', Comment, name='comment'),
]

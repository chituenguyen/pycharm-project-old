from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
]

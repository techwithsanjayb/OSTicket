from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'TKTUsers'

urlpatterns = [
    path('', home,name="home"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_login', user_login_view, name='user_login'),
]

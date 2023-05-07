from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'TKTAgent'

urlpatterns = [
    # path('', home, name="home"),
    path('agent_login', agent_login, name="agent_login"),
    # path('admin_dashboard', admin_dashboard, name="admin_dashboard"),
    # path('admin_logout', admin_logout, name="admin_logout"),
    ]
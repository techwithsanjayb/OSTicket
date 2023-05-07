from django.contrib import admin
from django.urls import path, include
from TKTAgent.views import *

app_name = 'TKTAgent'

urlpatterns = [
    path('agent_login', agent_login, name="agent_login"),
    path('agent_dashboard', agent_dashboard, name="agent_dashboard"),
    path('view_tickets_list_agent', view_tickets_list_agent, name="view_tickets_list_agent"),
    path('agent_resolve_ticket/<int:id>', agent_resolve_ticket, name="agent_resolve_ticket"),
]
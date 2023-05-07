from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'TKTAdmin'

urlpatterns = [
    path('', home, name="home"),
    path('admin_login', admin_login, name="admin_login"),
    path('admin_dashboard', admin_dashboard, name="admin_dashboard"),
    path('admin_logout', admin_logout, name="admin_logout"),

    path('view_agent_role', view_agent_role, name="view_agent_role"),
    path('create_agent_role', create_agent_role, name="create_agent_role"),
    path('edit_agent_role/<int:id>', edit_agent_role, name="edit_agent_role"),

    path('view_category', view_category, name="view_category"),
    path('create_category', create_category, name="create_category"),
    path('edit_category/<int:id>', edit_category, name="edit_category"),

    path('view_ticket_status_choice', view_ticket_status_choice, name="view_ticket_status_choice"),
    path('create_ticket_status_choice', create_ticket_status_choice, name="create_ticket_status_choice"),
    path('edit_ticket_status_choice/<int:id>', edit_ticket_status_choice, name="edit_ticket_status_choice"),

    path('view_technology_stack', view_technology_stack, name="view_technology_stack"),
    path('create_technology_stack', create_technology_stack, name="create_technology_stack"),
    path('edit_technology_stack/<int:id>', edit_technology_stack, name="edit_technology_stack"),

    path('view_Issue_Category', view_Issue_Category, name="view_Issue_Category"),
    path('create_Issue_Category', create_Issue_Category, name="create_Issue_Category"),
    path('edit_Issue_Category/<int:id>', edit_Issue_Category, name="edit_Issue_Category"),

    path('view_agent_list', view_agent_list, name="view_agent_list"),
    path('create_agent_list', create_agent_list, name="create_agent_list"),
    path('edit_agent_list/<int:id>', edit_agent_list, name="edit_agent_list"),


    path('view_tickets_list', view_tickets_list, name="view_tickets_list"),
    path('assign_ticket/<int:id>', assign_ticket, name="assign_ticket"),


]

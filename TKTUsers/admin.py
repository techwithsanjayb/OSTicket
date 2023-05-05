from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(technology_stack)
admin.site.register(TicketDetail)
admin.site.register(Ticket_status_choice)
admin.site.register(Ticket_status)
admin.site.register(Agent_Role)
admin.site.register(Agent)
admin.site.register(Issue_Category)


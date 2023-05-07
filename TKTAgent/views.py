# Create your views here.
from django.shortcuts import render, redirect
from TKTAdmin.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from TKTUsers.models import *


def agent_login(request):
    if request.method == 'POST':
        AgentLoginForm_obj = UserLoginForm(request=request, data=request.POST)
        if AgentLoginForm_obj.is_valid():
            uname = AgentLoginForm_obj.cleaned_data['username']
            passwd = AgentLoginForm_obj.cleaned_data['password']
            user = authenticate(username=uname, password=passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('TKTAgent:agent_dashboard')
            else:
                messages.error(request, "Agent does not exist")
                return render(request, 'TKTAgent/agent_login.html', {'AgentLoginForm_obj': AgentLoginForm_obj})
        else:
            messages.error(request, "Invalid Details . Please login with correct details")
            return render(request, 'TKTAgent/agent_login.html', {'AgentLoginForm_obj': AgentLoginForm_obj})
    else:
        AgentLoginForm_obj = UserLoginForm()
        return render(request, 'TKTAgent/agent_login.html', {'AgentLoginForm_obj': AgentLoginForm_obj})


def agent_dashboard(request):
    return render(request, 'TKTAgent/agent_dashboard.html')


def view_tickets_list_agent(request):
    Agent_TicketDetail_obj = TicketDetail.objects.filter(ticket_assigned_to=2,ticket_status = 2)
    return render(request, 'TKTAgent/agent_ticket_list.html', {'Agent_TicketDetail_obj': Agent_TicketDetail_obj})


def agent_resolve_ticket(request, id):
    if request.method == "POST":
        TicketDetail_obj = TicketDetail.objects.get(pk=id)
        Ticket_Form_obj = Ticket_Form_Agent(request.POST, instance=TicketDetail_obj)
        if Ticket_Form_obj.is_valid():
            temp_obj = Ticket_Form_obj.save(commit=False)
            temp_obj.ticket_status = Ticket_Form_obj.cleaned_data['ticket_status']
            temp_obj.save()

            messages.success(request, "Resolved  Successfully")
            return redirect('TKTAgent:view_tickets_list_agent')
        else:
            messages.error(request, "Invalid Data ")
            return render(request, 'TKTAgent/resolve_Ticket.html',
                          {'Ticket_Form_obj': Ticket_Form_obj})
    else:
        TicketDetail_obj = TicketDetail.objects.get(pk=id)
        Ticket_Form_obj = Ticket_Form_Agent(instance=TicketDetail_obj)
        return render(request, 'TKTAgent/resolve_Ticket.html',
                      {'Ticket_Form_obj': Ticket_Form_obj})

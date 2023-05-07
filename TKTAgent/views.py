# Create your views here.
from django.shortcuts import render, redirect
from TKTUsers.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


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

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from TKTAdmin.forms import *


# Create your views here.
def home(request):
    return user_signup(request)

##############################################


def user_signup(request):
    if request.method == 'POST':
        UserSignupForm_obj = UserSignupForm(request.POST)
        if UserSignupForm_obj.is_valid():
            UserSignupForm_obj.save()
            messages.success(request, "You are successfully registered")
            return redirect('TKTUsers:user_signup')
        else:
            return render(request, 'TKTUsers/user_signup.html', {'UserSignupForm_obj': UserSignupForm_obj})
    else:
        UserSignupForm_obj = UserSignupForm()
        return render(request, 'TKTUsers/user_signup.html', {'UserSignupForm_obj': UserSignupForm_obj})


##############################################

def user_login_view(request):

    if request.method == 'POST':
        UserLoginForm_obj = UserLoginForm(
            request=request, data=request.POST)
        if UserLoginForm_obj.is_valid():
            uname = UserLoginForm_obj.cleaned_data['username']
            passwd = UserLoginForm_obj.cleaned_data['password']
            user = authenticate(username=uname, password=passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('TKTUsers:user_create_ticket')
            else:
                messages.error(request, "User does not exist")
                return redirect('TKTUsers:user_login')
        else:
            messages.error(
                request, "Invalid Details . Please login with correct details")
            return redirect('TKTUsers:user_login')
    else:
        UserLoginForm_obj = UserLoginForm()
        return render(request, 'TKTUsers/user_login.html', {'UserLoginForm_obj': UserLoginForm_obj})

##############################################

def user_create_ticket(request):
    print('##############################')
    print(request.user)
    if request.method=='POST':
        Ticket_Form_obj = Ticket_Form(request.POST)
        if Ticket_Form_obj.is_valid():
            print("Valid DaTA")
            temp_obj = Ticket_Form_obj.save(commit=False)
            temp_obj.ticket_raised_by = request.user
            temp_obj.save()
            messages.success(request,"Created Successfully")
            return redirect('TKTUsers:user_create_ticket')
        else:
            print("INVALID DaTA")
            print(Ticket_Form_obj)
            messages.error(request, "Invalid Details")
            return render(request, 'TKTUsers/user_create_ticket.html', {'Ticket_Form_obj': Ticket_Form_obj})
    else:
        Ticket_Form_obj = Ticket_Form()
        return render(request, 'TKTUsers/user_create_ticket.html',{'Ticket_Form_obj':Ticket_Form_obj})


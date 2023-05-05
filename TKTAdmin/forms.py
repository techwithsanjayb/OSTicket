from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.forms import ModelForm
from TKTUsers.models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Enter Your Username", max_length=30, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Username', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'style': 'border-color: grey;', 'placeholder': 'Enter Password ',
               'class': 'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = ['username', ]


######################################################################################


class AgentRoleForm(forms.ModelForm):
    Agent_Role_name = forms.CharField(label="Enter Role", max_length=30, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Username', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = Agent_Role
        fields = ['Agent_Role_name', ]


######################################################################################

class CategoryForm(forms.ModelForm):
    Category_title = forms.CharField(label="Enter Category", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Username', 'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = Category
        fields = ['Category_title', ]


######################################################################################

class Ticket_status_choiceForm(forms.ModelForm):
    status_name = forms.CharField(label="Enter Status Name ", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Status Name',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = Ticket_status_choice
        fields = ['status_name', ]


######################################################################################

class technology_stackForm(forms.ModelForm):
    technology_name = forms.CharField(label="Enter Technology Name ", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Technology Name',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = technology_stack
        fields = ['technology_name', ]


######################################################################################

class Issue_CategoryForm(forms.ModelForm):
    Issue_Category_name = forms.CharField(label="Enter Issue Category Name ", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Issue Category Name ',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    class Meta:
        model = Issue_Category
        fields = ['Issue_Category_name', ]

######################################################################################

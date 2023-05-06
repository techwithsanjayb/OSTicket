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


class AgentForm(forms.ModelForm):
    Agent_name = forms.CharField(label="Enter Agent Name ", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Agent Name',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))
    Agent_status_choice = (
        ('Active', 'ACTIVE'), ('Deactivated', 'DEACTIVATED'))

    Agent_status = forms.ChoiceField(
        widget=forms.Select(
            attrs={'style': 'border-radius:6px', 'class': 'form-select'}),
        choices=Agent_status_choice)

    Agent_role = forms.ModelChoiceField(required=True, queryset=Agent_Role.objects.all(),
                                        widget=forms.Select(
                                            attrs={'class': 'form-control', 'id': 'solutionCategory',
                                                   'autocomplete': 'off'}))

    Agent_expert = forms.ModelChoiceField(required=True, queryset=technology_stack.objects.all(),
                                          widget=forms.Select(
                                              attrs={'class': 'form-control', 'id': 'technology_stack',
                                                     'autocomplete': 'off'}))

    class Meta:
        model = Agent
        fields = ['Agent_name', 'Agent_role', 'Agent_status', 'Agent_expert']


######################################################################################

class Ticket_Form(forms.ModelForm):
    websitename = forms.CharField(label="Enter Website Name", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Website  Name',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    websiteurl = forms.CharField(label="Enter Website URL", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Website URL',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    website_description = forms.CharField(label="Enter Website URL", max_length=100, widget=forms.TextInput(
        attrs={'style': 'border-color:grey', 'placeholder': 'Enter Website URL',
               'class': 'form-control form-control-lg',
               'autocomplete': 'off'}))

    website_category = forms.ModelChoiceField(required=True, queryset=Category.objects.all(),
                                          widget=forms.Select(
                                              attrs={'class': 'form-control', 'id': 'website_category',
                                                     'autocomplete': 'off'}))

    Issue_Related_To = forms.ModelChoiceField(required=True, queryset=Issue_Category.objects.all(),
                                              widget=forms.Select(
                                                  attrs={'class': 'form-control', 'id': 'Issue_Related_To',
                                                         'autocomplete': 'off'}))

    categories = forms.ModelMultipleChoiceField(queryset=technology_stack.objects.all(), widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = TicketDetail
        fields = ['websitename', 'websiteurl', 'website_description', 'website_technology', 'website_category',
                  'Issue_Related_To']

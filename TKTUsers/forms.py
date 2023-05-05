from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserSignupForm(UserCreationForm):
    username = forms.CharField(label="Your Email ", max_length=30, widget=forms.TextInput(
        attrs={'style': 'border-color: grey;margin-bottom:20px', 'placeholder': 'Enter Your Email',
               'class': 'form-control form-control-lg', 'autocomplete': 'off'}))
    password1 = forms.CharField(label="Your Password ", max_length=30, widget=forms.PasswordInput(
        attrs={'style': 'border-color: grey;margin-bottom:20px', 'placeholder': 'Enter Your Password',
               'class': 'form-control form-control-lg', 'autocomplete': 'off'}))
    password2 = forms.CharField(label="Confirm Password ", max_length=30, widget=forms.PasswordInput(
        attrs={'style': 'border-color: grey;margin-bottom:20px', 'placeholder': 'Confirm Your Password',
               'class': 'form-control form-control-lg', 'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['username', ]

    def save(self, commit=True):
        user_obj = super(UserSignupForm, self).save(commit=False)
        user_obj.email = self.cleaned_data["username"]
        user_obj.save()
        return user_obj



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
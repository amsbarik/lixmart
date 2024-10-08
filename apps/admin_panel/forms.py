from django import forms
from django.contrib.auth.forms import AuthenticationForm

# admin login form
class CustomAdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label=''  # Hide label
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label=''  # Hide label
    )
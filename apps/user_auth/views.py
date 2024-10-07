from django.shortcuts import render

# Create your views here.
# admin login view
def is_superuser(user):
    return user.is_superuser
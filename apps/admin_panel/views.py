from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import CustomAdminLoginForm

from apps.user_auth.views import is_superuser


# Create your views here.

# admin login 
def admin_login(request):
    if request.method == 'POST':
        form = CustomAdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('dashboard')
                # return redirect('admin:index') #this django admin panel
    else:
        form = CustomAdminLoginForm()
    return render(request, 'admin_panel/admin_login.html', {'form': form})


# logout 
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_logout(request):
    logout(request)
    return redirect('index') 


# admin dashboard view
@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')






























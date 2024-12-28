from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout

from .models import  UserSetting
from .forms import UpdateUserForm,  UserProfileSettingForm, UserSocialSettingForm, UserGeneralSettingForm, UserPhotoForm, UserNameForm, UserMobileForm, UserEmailForm, UserPositionForm, UserLocationForm, UserIntroForm




# Create your views here.
def users(request):
    return HttpResponse('Hello User')


# admin login view
def is_superuser(user):
    return user.is_superuser

# user profile update
# def update_user(request):
#     if request.user.is_authenticated:
#         current_user = User.objects.get(id=request.user.id)
#         user_form = UpdateUserForm(request.POST or None, instance=current_user)
        
#         if user_form.is_valid():
#             user_form.save()
            
#             login(request, current_user)
#             messages.success(request, 'User has been updated!')
#             return redirect('index')
        
#         return render(request, 'update_user.html', {'user_form': user_form})
    
#     else:
#         messages.success(request, 'You must be login to access that page!')
#         return redirect('index')
    
# update user profile
@login_required
def update_user(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
            # login(request, user)
            messages.success(request, 'Profile updated successfully!')
            return redirect('index')  # Replace with your desired redirect.
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'user_auth/update_user.html', {'form': form})

# update user password 
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Keeps the user logged in after password change.
#             messages.success(request, "Your password has been updated successfully!")
#             return redirect('index')  # Replace with your desired redirect view.
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = PasswordChangeForm(user=request.user)
#     return render(request, 'user_auth/change_password.html', {'form': form})

@login_required
def change_password(request):
    print(f"User: {request.user}, Is superuser: {request.user.is_superuser}, Authenticated: {request.user.is_authenticated}")
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change.
            messages.success(request, "Your password has been updated successfully!")
            return redirect('index')  # Replace with your desired redirect view.
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'user_auth/change_password.html', {'form': form})



# user profile settings view /////////////////////////////////
@login_required
@user_passes_test(is_superuser)
def user_profile_setting_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            profile_form = UserProfileSettingForm()
        else:
            user_setting = UserSetting.objects.get(id=pk)
            profile_form = UserProfileSettingForm(instance=user_setting)
            
        return render(request, 'admin_panel/user_auth/user_profile_setting_form.html', {'profile_form': profile_form})
    
    else:
        if pk == 0:
            profile_form = UserProfileSettingForm(request.POST, request.FILES)
        else:
            user_setting = UserSetting.objects.get(id=pk)
            profile_form = UserProfileSettingForm(request.POST, request.FILES, instance=user_setting)
            
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile settings updated successfully!')
            
        return redirect('user_account_setting')
    
# single field form ///////////////
@login_required
@user_passes_test(is_superuser)
def user_photo_form(request, pk):
    
    user_setting = UserSetting.objects.get(id=pk)
    if request.method == 'GET':
        user_setting = UserSetting.objects.get(id=pk)
        profile_form = UserPhotoForm(instance=user_setting)
            
        return render(request, 'admin_panel/user_auth/user_account_setting.html', {'profile_form': profile_form, 'user_setting': user_setting})
    
    else:
        user_setting = UserSetting.objects.get(id=pk)
        profile_form = UserPhotoForm(request.POST, request.FILES, instance=user_setting)
            
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile photo updated successfully!')
            
        return redirect('user_account_setting')
    
    

# social setting view //////////////////////////////
@login_required
@user_passes_test(is_superuser)
def user_social_setting_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            social_form = UserSocialSettingForm()
        else:
            user_setting = UserSetting.objects.get(id=pk)
            social_form = UserSocialSettingForm(instance=user_setting)
            
        return render(request, 'admin_panel/user_auth/user_social_setting_form.html', {'social_form': social_form})
    
    else:
        if pk == 0:
            social_form = UserSocialSettingForm(request.POST, request.FILES)
        else:
            user_setting = UserSetting.objects.get(id=pk)
            social_form = UserSocialSettingForm(request.POST, request.FILES, instance=user_setting)
            
        if social_form.is_valid():
            social_form.save()
            messages.success(request, 'Your social settings updated successfully!')
            
        return redirect('user_setting_form_all')
    
    
# general setting view
@login_required
@user_passes_test(is_superuser)
def user_general_setting_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            general_form = UserGeneralSettingForm()
        else:
            user_setting = UserSetting.objects.get(id=pk)
            general_form = UserGeneralSettingForm(instance=user_setting)
            
        return render(request, 'admin_panel/user_auth/user_general_setting_form.html', {'general_form': general_form})
    
    else:
        if pk == 0:
            general_form = UserGeneralSettingForm(request.POST, request.FILES)
        else:
            user_setting = UserSetting.objects.get(id=pk)
            general_form = UserGeneralSettingForm(request.POST, request.FILES, instance=user_setting)
            
        if general_form.is_valid():
            general_form.save()
            messages.success(request, 'Your general settings updated successfully!')
            
        return redirect('user_setting_form_all')
    
    
    
# setting all view 
@login_required
@user_passes_test(is_superuser)
def user_account_setting(request):
    
    user_setting = UserSetting.objects.first()
    
    profile_form = UserProfileSettingForm(instance=user_setting)
    
    context = {
        'profile_form': profile_form,
        'user_setting': user_setting,
    }
        
    return render(request, 'admin_panel/user_auth/user_account_setting.html', context)


# setting all view 
@login_required
@user_passes_test(is_superuser)
def user_setting_form_all(request):
    
    user_setting = UserSetting.objects.first()
    
    social_form = UserSocialSettingForm(instance=user_setting)
    general_form = UserGeneralSettingForm(instance=user_setting)
    
    context = {
        'social_form': social_form,
        'general_form': general_form,
        'user_setting': user_setting,
    }
        
    return render(request, 'admin_panel/user_auth/user_setting_form_all.html', context)
    
   
  
  


    
 
   
   
   
   
   
   
   
   
   
   
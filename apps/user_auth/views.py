from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse

from .models import  UserSetting
from .forms import  UserProfileSettingForm, UserSocialSettingForm, UserGeneralSettingForm, UserPhotoForm, UserNameForm, UserMobileForm, UserEmailForm, UserPositionForm, UserLocationForm, UserIntroForm

# Create your views here.
def users(request):
    return HttpResponse('Hello User')


# admin login view
def is_superuser(user):
    return user.is_superuser




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
    
   
   
   
   
   
   
   
   
   
   
   
   
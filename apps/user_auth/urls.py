from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.users, name='users'),
    
    # user_setting_form 
    path('acount/settings/', views.user_account_setting, name='user_account_setting'),
    path('settings/update/', views.user_setting_form_all, name='user_setting_form_all'),
    path('profile/settings/update/<int:pk>/', views.user_profile_setting_form, name='user_profile_setting_form'),
    path('social/settings/update/<int:pk>/', views.user_social_setting_form, name='user_social_setting_form'),
    path('general/settings/update/<int:pk>/', views.user_general_setting_form, name='user_general_setting_form'),
    
    # single filed urls 
    path('account/photo/update/<int:pk>/', views.user_photo_form, name='user_photo_form'),
    
]

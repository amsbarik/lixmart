from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.

admin.site.register(Profile)


# Mix Profile info and user info 
class ProfileInline(admin.StackedInline):
    model = Profile
    
# Extend user model 
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]
    
# Unregister the old way 
admin.site.unregister(User)

# Re-Register the new way 
admin.site.register(User, UserAdmin)
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Team, Role, Gender, UserSetting

class TeamForm(forms.ModelForm):
    
    class Meta:
        model = Team
        fields = ['name', 'profile_img', 'mobile', 'email', 'nid', 'passport', 'gender', 'address', 'nationality', 'religion', 'birth_date', 'blood', 'join_date', 'rejoin_date', 'role', 'skill', 'resume', 'portfolio_url', 'github_url', 'linkedin_url', 'facebook_url', 'intro']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'profile_img' : forms.FileInput(attrs={'class': 'form-control',  'placeholder': 'Upload your photo'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter active number'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid email'}),
            'nid' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your nid'}),
            'passport' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your passport'}),
            'gender' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'nationality' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your nationality'}),
            'religion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your religion'}),
            'birth_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blood group'}),
            'join_date' : forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rejoin_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'role' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'skill' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your skills'}),
            'resume' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload your resume'}),
            'portfolio_url' : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter portfolio url'}),
            'github_url' : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter github url'}),
            'linkedin_url' : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter linkedin url'}),
            'facebook_url' : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter facebook url'}),
            'intro' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your intro'}),
        }
        
        def clean_join_date(self):
            join_date = self.cleaned_data.get('join_date')
            if not join_date:
                raise forms.ValidationError("Join date is required.")
            return join_date
        
        
# user sttings form /////////////////////////////////////
class UserProfileSettingForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['user_photo', 'name', 'position', 'mobile', 'email', 'location', 'intro'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
        
class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['user_photo'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserNameForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['name'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserPositionForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['position'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserMobileForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['mobile'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['email'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['location'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))

class UserIntroForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['intro'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
        
        
# user social setting form ////////////////////
class UserSocialSettingForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['website_url', 'linkedin_url', 'github_url', 'stackoverflow_url', 'twitter_url', 'reddit_url', 'facebook_url']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
        

# user general setting form 
class UserGeneralSettingForm(forms.ModelForm):
    class Meta:
        model = UserSetting
        fields = ['logo', 'fav_icon', 'index_title', 'index_meta_kewords', 'short_desc']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
            
            


# update user form 
# class UpdateUserForm(UserChangeForm):
#     email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
#     class Meta:
#         model: User 
#         fields = ('username', 'first_name', 'last_name', 'email')
        
#     def __init__(self, *args, **kwargs):
#         super(UpdateUserForm, self).__init__(*args, **kwargs)
        
#         self.fields['username'].widget.attrs['class'] = 'form-control'
        
class UpdateUserForm(UserChangeForm):
    # hide password 
    password = None
    
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}) )
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField( label='',  max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}) )

    class Meta:
        model = User  # Fixed from `model: User` to `model = User`
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

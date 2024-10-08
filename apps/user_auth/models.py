from django.db import models
from datetime import datetime


# Create your models here.
class BaseUser(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Role(BaseUser):
    
    def __str__(self):
        return self.name
    
    
class Gender(BaseUser):
    
    def __str__(self):
        return self.name


class Team(BaseUser):
    member_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='developer_photo/')
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    nid = models.CharField(max_length=30)
    passport = models.CharField(max_length=30, null=True, blank=True)
    gender = models.ForeignKey(Gender, related_name='gender', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    blood = models.CharField(max_length=6,blank=True, null=True)
    join_date = models.DateTimeField()
    rejoin_date = models.DateTimeField(blank=True, null=True)
    role = models.ForeignKey(Role, related_name='employee_role', on_delete=models.CASCADE)
    skill = models.TextField()
    
    resume = models.FileField(upload_to='developer_resume/', default='resume.pdf')
    portfolio_url = models.URLField(max_length=200, blank=True,  default='https://www.yourdomain.com')
    github_url = models.URLField(max_length=200, blank=True,  default='https://www.github.com/')
    linkedin_url = models.URLField(max_length=200, blank=True,  default='https://www.linkedin.com/')
    stackoverflow_url = models.URLField(max_length=200, blank=True,  default='https://www.stackoverflow.com/')
    reddit_url = models.URLField(max_length=200, blank=True,  default='https://www.reddit.com/')
    facebook_url = models.URLField(max_length=200, blank=True, default='https://www.facebook.com/')
    
    intro = models.TextField(blank=True, null=True, default='I am ')
    
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.member_id:
            last_member = Team.objects.all().order_by('id').last()
            if last_member:
                last_id = int(last_member.member_id.replace('DEV', ''))
                new_id = last_id + 1
            else:
                new_id = 4101
            self.member_id = f'DEV{new_id}'
        super(Team, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    





# user settings model
class UserSetting(BaseUser):
    
    user_photo = models.ImageField(upload_to='users/', blank=True, default='users/user-photo.jpg')
    position = models.CharField(max_length=50, blank=True)
    intro = models.TextField(blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    website_url = models.URLField(default='https://', blank=True)
    linkedin_url = models.URLField(default='https://', blank=True)
    github_url = models.URLField(default='https://', blank=True)
    stackoverflow_url = models.URLField(default='https://', blank=True)
    twitter_url = models.URLField(default='https://', blank=True)
    reddit_url = models.URLField(default='https://', blank=True)
    facebook_url = models.URLField(default='https://', blank=True)
    
    logo = models.ImageField(upload_to='users/', blank=True, default='users/logo.jpg')
    fav_icon = models.ImageField(upload_to='users/', blank=True, default='users/fav-icon.png')
    index_title = models.CharField(max_length=254, blank=True)
    index_meta_kewords = models.TextField(blank=True)
    short_desc = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Site Settings"
    
    
    
    
    
    









































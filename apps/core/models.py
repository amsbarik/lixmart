from django.db import models

# Create your models here.
class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveBigIntegerField(null=True, blank=True)
    
    class Meta:
        abstract = True
        
        
# Top slider model     
class TopSlider(CoreModel):
    heading = models.CharField(max_length=200, blank=True, help_text="Heading of the slide")
    image = models.ImageField(upload_to='slider_images/', help_text="Image for the slide")
    short_desc = models.TextField(blank=True, help_text="Description for the slide")
    btn_txt = models.CharField(max_length=100, blank=True, help_text="Text for the button")
    link_url = models.URLField(max_length=200, blank=True, help_text="URL the button will link to")

    def __str__(self):
        return self.heading


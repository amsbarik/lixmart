from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import TopSlider

class TopSliderForm(forms.ModelForm):
    class Meta:
        model = TopSlider
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'
        
        
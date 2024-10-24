from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'
        

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
        # fields = ['title', 'slug', 'category', 'subcategory', 'price', 'discount_price', 'description', 'view_img', 'thum_img']
        # fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
        # self.fields['subcategory'].queryset = Category.objects.none()

        # if 'category' in self.data:
        #     try:
        #         category_id = int(self.data.get('category'))
        #         self.fields['subcategory'].queryset = Category.objects.filter(parent_id=category_id)
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['subcategory'].queryset = self.instance.category.children.all()

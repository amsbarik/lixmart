from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.products.models import Product
# Create your models here.


# class Category(MPTTModel):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(unique=True)
#     parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
#     icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     order = models.PositiveBigIntegerField(null=True, blank=True)

#     class MPTTMeta:
#         order_insertion_by = ['name']

#     def __str__(self):
#         return self.name

#     def total_products(self):
#         # Include products in the current category and all subcategories
#         return Product.objects.filter(category__in=self.get_descendants(include_self=True)).count()



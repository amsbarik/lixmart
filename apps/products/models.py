from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

from apps.core.models import CoreModel


# category model
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



class Category(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank slug for automatic generation
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveBigIntegerField(null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def total_products(self):
        # Include products in the current category and all subcategories
        return Product.objects.filter(category__in=self.get_descendants(include_self=True)).count()

    # Override the save method to generate slug automatically
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not provided
            self.slug = slugify(self.name)
            # Ensure slug is unique
            unique_slug = self.slug
            num = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)





# size model 
class Size(CoreModel):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Brand model 
class Brand(CoreModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Product model 
class Product(CoreModel):
    title = models.CharField(max_length=255)  # Product Title
    slug = models.SlugField(max_length=255, unique=True)  # For breadcrumb URL, SEO-friendly
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Discount price
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # Average rating
    total_reviews = models.IntegerField(default=0)  # Total review count
    available_stock = models.IntegerField(default=0)  # Available quantity in stock

    # Image gallery
    main_image = models.ImageField(upload_to='product_images/')  # Main product image
    additional_images = models.ManyToManyField('ProductImage', blank=True)  # Related images

    # Color options with an associated image
    colors = models.ManyToManyField('Color', related_name='products')
    
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')

    # Category for breadcrumbs
    # from apps.categories.models import Category
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.title
    
    


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')  # Additional product images
    alt_txt = models.CharField(max_length=255)  # Alt text for the image

    def __str__(self):
        return self.alt_text

    
# color model 
class Color(CoreModel):
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='color_images/', blank=True, null=True)  # Color image thumbnail

    def __str__(self):
        return self.name
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist"


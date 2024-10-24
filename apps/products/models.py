from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

from apps.core.models import CoreModel


# category model
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
    



# Product model 
# class Product(CoreModel):
#     title = models.CharField(max_length=255)  # Product Title
#     slug = models.SlugField(max_length=255, unique=True, blank=True)  # For breadcrumb URL, SEO-friendly
#     description = models.TextField()  # Product description
#     shipping_txt = models.TextField(default='shipping policy')  # Product description
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Discount price
#     rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # Average rating
#     total_reviews = models.IntegerField(default=0)  # Total review count
#     available_stock = models.IntegerField(default=0)  # Available quantity in stock

#     # Image gallery
#     view_img = models.ImageField(upload_to='product_images/')  # Main product image
#     thum_img = models.ManyToManyField('ProductImage', blank=True)  # Related images

#     # Color options with an associated image
#     colors = models.ManyToManyField(Color, related_name='products', blank=True)
    
#     size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

#     # Category for breadcrumbs
#     # from apps.categories.models import Category
#     # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

#     # Override the save method to generate slug automatically
#     def save(self, *args, **kwargs):
#         if not self.slug:  # Generate slug only if it's not provided
#             self.slug = slugify(self.name)
#             # Ensure slug is unique
#             unique_slug = self.slug
#             num = 1
#             while Product.objects.filter(slug=unique_slug).exists():
#                 unique_slug = f'{self.slug}-{num}'
#                 num += 1
#             self.slug = unique_slug
#         super().save(*args, **kwargs)
        
        
#     def __str__(self):
#         return self.title
    
    

class Product(CoreModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    shipping_txt = models.TextField(default='shipping policy')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, blank=True)
    total_reviews = models.IntegerField(default=0, blank=True)
    available_stock = models.IntegerField(default=0)
    
    sales_count = models.IntegerField(default=0, blank=True)  # Field to track sales count

    # Image gallery
    view_img = models.ImageField(upload_to='product_images/')
    # thum_img = models.ManyToManyField('ProductImage', blank=True)

    # Category and Subcategory
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    # subcategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_products')

    # Other fields...
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products', blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            num = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# Wishlist model 
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist"
    


# Cart model 
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.quantity} x {self.product.title}'
    
    
    
# class Cart:
    
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get('cart')
#         if not cart:
#             # Initialize an empty cart
#             cart = self.session['cart'] = {}
#         self.cart = cart

#     def add(self, product):
#         if str(product.id) not in self.cart:
#             self.cart[str(product.id)] = {'quantity': 1, 'price': str(product.price)}
#         else:
#             self.cart[str(product.id)]['quantity'] += 1
        
#         self.save()

#     def save(self):
#         self.session.modified = True  # Mark the session as modified to save changes

#     def get_total_price(self):
#         return sum(int(item['price']) * item['quantity'] for item in self.cart.values())
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.quantity} x {self.product.title}'


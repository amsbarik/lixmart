from django.urls import path 
from .import views

urlpatterns = [
    
    
    #  path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    
    # admin panel urls 
    path('list/', views.product_list, name='product_list'),
    path('form/', views.product_form, name='product_form'),
    path('update/<int:pk>/', views.product_form, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    
    path('<slug:slug>/', views.product_details, name='product_details'),
    
]
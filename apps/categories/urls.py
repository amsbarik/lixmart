from django.urls import path
from . import views


urlpatterns = [
    
    
    # admin panel urls
    path('all/', views.category_all, name='category_all'),
    path('form/', views.category_form, name='category_form'),
    path('update/<int:pk>/', views.category_form, name='category_update'),
    path('delete/<int:pk>/', views.category_delete, name='category_delete'),
    
    
    # path('categories/', views.category_view, name='category_view'),
    
    
    
    path('<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
]

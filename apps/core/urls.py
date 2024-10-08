from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # admin panel urls
    path('sliders/', views.top_slider_all, name='top_slider_all'),
    path('sliders/form/', views.top_slider_form, name='top_slider_form'),
    path('slider/update/<int:pk>/', views.top_slider_form, name='top_slider_update'),
    path('slider/delete/<int:pk>/', views.top_slider_delete, name='top_slider_delete'),
]


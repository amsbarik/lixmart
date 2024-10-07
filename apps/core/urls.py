from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # admin panel urls
    path('sliders/', views.top_silder_all, name='top_silder_all'),
    path('sliders/form/', views.top_silder_form, name='top_silder_form'),
    path('sliders/update/<int:pk>/', views.top_silder_form, name='top_silder_update'),
    path('sliders/delete/<int:pk>/', views.top_silder_delete, name='top_silder_delete'),
]


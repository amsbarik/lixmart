from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from .forms import TopSliderForm
from .models import TopSlider
from apps.user_auth.views import is_superuser
from apps.products.models import Category, Product

# Create your views here.
def index(request):
    # Fetch active top sliders
    top_sliders = TopSlider.objects.filter(is_active=True).order_by('order')
    
    # Fetch all categories
    categories = Category.objects.filter(is_active=True).order_by('created_at')

    # Fetch best-selling products (top 10 by sales count)
    best_selling_products = Product.objects.order_by('-sales_count')[:20]  # Get top 10 best-selling products

    # Fetch new arrivals (products added in the last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    new_arrivals = Product.objects.filter(created_at__gte=thirty_days_ago).order_by('-created_at')
    
    # Fetch products from a specific category (e.g., Panjabi)
    panjabi_category = Category.objects.get(slug='panjabi')  # Assuming 'panjabi' slug
    panjabi_products = Product.objects.filter(category=panjabi_category)


    context = {
        'top_sliders': top_sliders,
        'categories': categories,
        
        'best_selling_products': best_selling_products,  # Add best-selling products to context
        'new_arrivals': new_arrivals,  # Add new arrivals to context
        'panjabi_products': panjabi_products,  # Pass Panjabi products to the template
        
    }

    return render(request, 'core/index.html', context)








# admin panel views here ///////////////////////////////////
# Top all slider view 
@login_required
@user_passes_test(is_superuser)
def top_slider_all(request):
    top_sliders = TopSlider.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/top_slider_all.html', {'top_sliders': top_sliders})


# TopSlider create & update form view 
@login_required
@user_passes_test(is_superuser)
def top_slider_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = TopSliderForm()
        else:
            top_slider = TopSlider.objects.get(id=pk)
            form = TopSliderForm(instance=top_slider)
            
        return render(request, 'admin_panel/core/top_slider_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = TopSliderForm(request.POST, request.FILES)
        else:
            top_slider = TopSlider.objects.get(id=pk)
            form = TopSliderForm(request.POST, request.FILES, instance=top_slider)

        if form.is_valid():
            form.save()
            
        return redirect('top_slider_all')


# TopSlider delete view 
@login_required
@user_passes_test(is_superuser)
def top_slider_delete(request, pk):
    top_silder = TopSlider.objects.get(id=pk)
    top_silder.delete()
    return redirect('top_slider_all')


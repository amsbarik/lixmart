from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from .forms import TopSliderForm
from .models import TopSlider
from apps.user_auth.views import is_superuser
from apps.products.models import Category

# Create your views here.
def index(request):
    top_sliders = TopSlider.objects.filter(is_active=True).order_by('order')
    categories = Category.objects.order_by('created_at').all()
    context = {
        'top_sliders': top_sliders,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)








# admin panel TopSlider views here ///////////////////////////////////
# @login_required
# @user_passes_test(is_superuser)
def top_slider_all(request):
    top_sliders = TopSlider.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/core/top_slider_all.html', {'top_sliders': top_sliders})


# TopSlider create & update form view 
# @login_required
# @user_passes_test(is_superuser)
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
# @login_required
# @user_passes_test(is_superuser)
def top_slider_delete(request, pk):
    top_silder = TopSlider.objects.get(id=pk)
    top_silder.delete()
    return redirect('top_slider_all')


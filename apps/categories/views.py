from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView  
# from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.products.models import Category, Product  # Assuming I have a Product model
from .forms import CategoryForm
from apps.user_auth.views import is_superuser

# Create your views here.


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/product_store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object

        # Get products related to the category and its subcategories
        products = Product.objects.filter(category__in=category.get_descendants(include_self=True))

        # Add additional filters if needed (price, color, size, etc.)
        context['products'] = products
        return context

  
# ListView 
# class CategoryListView(ListView):
#     model = Category
#     template_name = 'store/category_list.html'
#     context_object_name = 'categories'

#     def get_queryset(self):
#         # Fetch only active categories (you can modify the filter as needed)
#         return Category.objects.filter(parent__isnull=True, is_active=True).prefetch_related('children')


# def category_list_view(request):
#     # Fetch only top-level categories (parent categories)
#     top_categories = Category.objects.filter(parent=None, is_active=True).order_by('order')
    
#     context = {
#         'top_categories': top_categories,
#     }
#     return render(request, 'core/index.html', context)

# def category_view(request):
#     # Fetch only parent categories
#     categories = Category.objects.filter(parent__isnull=True)
#     return render(request, 'admin_panel/categories/categories.html', {'categories': categories})




# admin panel views here ///////////////////////////////////
# all Category views
@login_required
@user_passes_test(is_superuser)
def category_all(request):
    categories = Category.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/categories/category_all.html', {'categories': categories})


# Category create & update form view 
@login_required
@user_passes_test(is_superuser)
def category_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = CategoryForm()
        else:
            category = get_object_or_404(Category, id=pk)
            form = CategoryForm(instance=category)
        
        return render(request, 'admin_panel/categories/category_form.html', {'form': form})
    
    else:  # POST request
        if pk == 0:
            form = CategoryForm(request.POST, request.FILES)
        else:
            category = get_object_or_404(Category, id=pk)
            form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            return redirect('category_all')  # Assuming you have a URL pattern named 'category_all'
        else:
            return render(request, 'admin_panel/categories/category_form.html', {'form': form})


# Category delete view 
@login_required
@user_passes_test(is_superuser)
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_all')


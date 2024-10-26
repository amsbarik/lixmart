from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


from apps.user_auth.views import is_superuser
from .forms import ProductForm
from .models import Product, Category


# Create your views here.
def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Get related products from the same category, excluding the current product
    related_products = Product.objects.filter(category=product.category).exclude(slug=slug)# [:8]  Limit to 8 or adjust as needed

    context = {
        'product': product,
        'related_products': related_products,
    }
    
    return render(request, 'products/product_details.html', context)



# load subcategories in product form view
# def load_subcategories(request):
#     category_id = request.GET.get('category_id')
#     subcategories = Category.objects.filter(parent_id=category_id).all()
#     return render(request, 'products/subcategory_dropdown_list_options.html', {'subcategories': subcategories})





# admin view start here 
# product list view 
@login_required
@user_passes_test(is_superuser)
def product_list(request):
    products = Product.objects.order_by('created_at').all()
    # products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, 'admin_panel/products/product_list.html', context)


# product create and update form view 
@login_required
@user_passes_test(is_superuser)
def product_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProductForm()
        else:
            product = get_object_or_404(Product, id=pk)
            form = ProductForm(instance=product)
            
        return render(request, 'admin_panel/products/product_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ProductForm(request.POST, request.FILES)
        else:
            product = get_object_or_404(Product, id=pk)
            form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            
        return redirect('product_list')
    
    # category_id = request.GET.get('category_id')
    # subcategories = Category.objects.filter(parent_id=category_id).all()
    # return render(request, 'products/subcategory_dropdown_list_options.html', {'subcategories': subcategories})


# from django.http import JsonResponse
# from .models import Category

# def product_form(request, pk=0):
#     if request.method == 'GET':
#         if pk == 0:
#             form = ProductForm()
#         else:
#             product = get_object_or_404(Product, id=pk)
#             form = ProductForm(instance=product)
            
#         return render(request, 'admin_panel/products/product_form.html', {'form': form})

#     elif request.method == 'POST' and request.is_ajax():
#         # Handle the AJAX request for subcategories
#         category_id = request.POST.get('category_id')
#         if category_id:
#             subcategories = Category.objects.filter(parent_id=category_id).values('id', 'name')
#             return JsonResponse(list(subcategories), safe=False)

#         return JsonResponse({'error': 'No category selected'}, status=400)

#     else:
#         # Handle form submission
#         if pk == 0:
#             form = ProductForm(request.POST, request.FILES)
#         else:
#             product = get_object_or_404(Product, id=pk)
#             form = ProductForm(request.POST, request.FILES, instance=product)

#         if form.is_valid():
#             form.save()
#             return redirect('product_list')

#         return render(request, 'admin_panel/products/product_form.html', {'form': form})


# Product delete view 
@login_required
@user_passes_test(is_superuser)
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_list')


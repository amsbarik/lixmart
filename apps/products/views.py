from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


from apps.user_auth.views import is_superuser
from .forms import ProductForm
from .models import Product, Category
from .cart import  Cart


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



# add to cart view 
# def add_to_cart(request, slug):
#     product = get_object_or_404(Product, slug=slug)
    
#     # Check if the product is already in the cart
#     cart_item, created = Cart.objects.get_or_create(
#         user=request.user,
#         product=product,
#     )

#     if not created:
#         # If the product is already in the cart, increase the quantity
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect('cart')  # Redirect to the cart page (or you can redirect back to the product or home page)


# def add_to_cart(request):
#     if request.method == 'POST' and request.is_ajax():
#         product_id = request.POST.get('product_id')
#         product = get_object_or_404(Product, id=product_id)
        
#         # Add or update the cart item
#         cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
        
#         # Retrieve updated cart items
#         cart_items = Cart.objects.filter(user=request.user)
        
#         # Render the updated cart HTML
#         cart_html = render_to_string('cart_popup.html', {'cart_items': cart_items})
        
#         return JsonResponse({'cart_html': cart_html}, status=200)
    
#     return JsonResponse({'error': 'Invalid request'}, status=400)


# def add_to_cart(request):
#     if request.method == 'POST':
#         slug = request.POST.get('slug')
#         product = get_object_or_404(Product, slug=slug)
        
#         # Assuming you have a Cart class managing cart items
#         cart = Cart(request)  # Assuming you're using a session-based cart
#         cart.add(product)  # Logic to add the product to the cart
        
#         # Render the updated cart HTML (ensure this is correctly defined)
#         cart_html = render_to_string('layouts/order_cart.html', {'cart': cart})
        
#         return JsonResponse({'cart_html': cart_html})
#     return JsonResponse({'error': 'Invalid request'}, status=400)


# def add_to_cart(request):
#     if request.method == 'POST':
#         slug = request.POST.get('slug')
#         product = get_object_or_404(Product, slug=slug)

#         # Create an instance of the cart
#         cart = Cart(request)

#         # Add the product to the cart
#         cart.add(product)

#         # Render the updated cart HTML
#         cart_html = render_to_string('layouts/order_cart.html', {'cart': cart})

#         # Send back the updated cart HTML in JSON format
#         return JsonResponse({'cart_html': cart_html})

#     return JsonResponse({'error': 'Invalid request'}, status=400)



def add_to_cart(request, slug):
    if request.method == 'POST':
        # Fetch the slug from the POST request
        slug = request.POST.get('slug')

        # Retrieve the product based on the slug
        product = get_object_or_404(Product, slug=slug)

        # Get the cart from the session
        cart = Cart(request)

        # Add the product to the cart
        cart.add(product=product)

        # Return success with cart data (if required)
        return JsonResponse({'status': 'success', 'message': f"{product.title} added to cart"})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



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


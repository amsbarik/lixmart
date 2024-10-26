from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from apps.products.models import Product


# Create your views here.
def cart_summary(request):
    # Get the cart 
    cart = Cart(request)
    cart_products = cart.get_prods
    
    return render(request, 'cart/cart_summary.html', {'cart_products': cart_products})



def cart_add(request):
    # Get the cart 
    cart = Cart(request)
    
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get stuff 
        product_id = int(request.POST.get('product_id'))
        
        # lookup product in DB 
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session 
        cart.add(product=product)
        
        # Get cart quantity 
        cart_quantity = cart.__len__()
        
        # return responce 
        # responce = JsonResponse({'Product Name': product.title})
        responce = JsonResponse({'qty': cart_quantity})
        return responce



def cart_update(request):
    pass




def cart_delete(request):
    pass

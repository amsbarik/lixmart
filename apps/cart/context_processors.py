from .cart import Cart

# Create a context processor so our cart work on all pages of this site
def cart(request):
    # Return the default data from our Cart
    return {'cart': Cart(request)}

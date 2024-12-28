from apps.products.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get the current session key if it exist 
        cart = self.session.get('session_key')
        
        # If the user is new, no session key, Create One
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure cart is available on all pages of site
        self.cart = cart
        
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
    def cart_total(self):
        # get product ids 
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        
        # get quantities 
        quantities = self.cart
        # {'4':3, '2': 5}
        # start counting at 0 
        total = 0
        for key, value in quantities.items():
            # convert key string into int, so we can do math 
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.discount_price is None:
                        total = total + (product.price * value)
                    else:
                        total = total + (product.discount_price * value)
                    
        return total 
                    
            
        
    # return cart total items
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        # Get ids from cart 
        product_ids = self.cart.keys()
        
        # use ids to lookup products in database model 
        products = Product.objects.filter(id__in=product_ids)
        
        # return those looked up products 
        return products
    
    # get quantity 
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        # like {'4': 3, '2': 5}
        
        # Get cart 
        ourcart = self.cart
        # update dictionary/cart 
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        thing = self.cart
        
        return thing
    
    def delete(self, product):
        # {'4': 3, '2':1}
        product_id = str(product)
        # delete from dictionary/cart 
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        
from home.models import Product

CART_NAME_SESSION = 'cart'

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart  = self.session.get(CART_NAME_SESSION)
        if not cart:
            cart = self.session[CART_NAME_SESSION] = {}
            print("="*90)
            print('the cart is initialize')
        self.cart = cart

    def __iter__(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product_name"] = product
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item
            

    def add(self,product,quantity):
        product_id = str(product.id)
        print("="*90)
        print(type(self.cart))
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        
    def save(self):
        self.session.modified = True

    def total_price(self):
        return sum([int(item['price'])*item['quantity'] for item in self.cart.values()])
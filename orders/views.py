from django.shortcuts import render ,get_object_or_404 , redirect
from django.views import View
from home.models import Product
from .cart import Cart
from orders.forms import CartAddForm
# Create your views here.

class CartView(View):
    def get(self,request):
        cart = Cart(request)
        return render(request,'orders/cart.html',{"carts":cart})
    

class AddCartView(View):
    form_class = CartAddForm
    def post(self,request,product_id):
        product = get_object_or_404(Product,id = product_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            cart = Cart(request)
            quantity = form.cleaned_data['quantity']
            cart.add(product,quantity)
            return redirect('orders:cart')
        
class RemoveCartView(View):
    def get(self,reques,product_id):
        product = get_object_or_404(Product,id=product_id)
        cart = Cart(reques)
        cart.remove(product)
        return redirect('orders:cart')




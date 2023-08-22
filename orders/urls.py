from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/',views.CartView.as_view(),name='cart'),
    path('cart/add/<int:product_id>',views.AddCartView.as_view(),name='add_cart'),
    path('cart/remove/<int:product_id>',views.RemoveCartView.as_view(),name='remove_cart'),
]
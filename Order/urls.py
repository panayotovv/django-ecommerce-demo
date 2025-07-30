from django.urls import path
from Order.views import CartView, CheckoutView, ClearCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart-view',),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout-view'),
    path('cart/clear/', ClearCartView.as_view(), name='clear-cart'),
]
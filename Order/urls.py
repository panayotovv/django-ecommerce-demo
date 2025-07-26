from django.urls import path
from Order.views import CartView, CheckoutView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart-view',),
    path('checkout/', CheckoutView.as_view(), name='checkout-view'),
]
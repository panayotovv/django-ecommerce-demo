from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from Order.forms import CartForm


class CartView(FormView):
    template_name = 'cart.html'
    form_class = CartForm
    success_url = reverse_lazy('checkout-view')

class CheckoutView(TemplateView):
    template_name = 'credit-card.html'

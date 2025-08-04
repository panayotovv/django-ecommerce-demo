from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from Order.forms import CartForm, CheckoutForm
from Order.models import Order, OrderItem
from Programs.models import Programs
from Shop.models import Product
from django.contrib import messages
import random

MODEL_MAPPER = {
    'product': Product,
    'program': Programs,
}

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, model_name, item_id):
        model_class = MODEL_MAPPER.get(model_name)
        product = get_object_or_404(model_class, pk=item_id)
        size = request.POST.get('size')

        if not size and product.category != 'equipment' and model_name != 'program':
            messages.error(request, "Please select a size.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

        cart = request.session.get('cart', {})

        key = f"{product.title}:{product.id}:{size}"

        if key in cart:
            cart[key]['quantity'] += 1
            price_per_item = float(cart[key]['price'])
            cart[key]['total_price'] = price_per_item * cart[key]['quantity']
        else:
            cart[key] = {
                'name': product.title,
                'price': str(product.price),
                'image': product.image_url,
                'quantity': 1,
                'total_price': product.price,
                'pk': product.pk,
                'category': product.category,
                'model': model_name,
                'size': size,
            }

        request.session['cart'] = cart
        request.session.modified = True

        if product.category == 'equipment' or model_name == 'program':
            messages.success(request, f"✅ '{product.title}' added to cart!")
        else:
            messages.success(request, f"✅ '{product.title}' (Size: {size}) added to cart!")

        return redirect(request.META.get('HTTP_REFERER', '/'))



class CartView(FormView):
    template_name = 'cart.html'
    form_class = CartForm
    success_url = reverse_lazy('checkout-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        total = sum(item['total_price'] for item in cart.values())
        tax = random.randint(5, 20)

        if not cart.items():
            tax = 0

        context['tax'] = tax
        context['cart'] = cart
        context['grand_total'] = f'{total:.2f}'
        context['total_after_tax'] = f'{total + tax:.2f}'
        return context

    def form_valid(self, form):
        user = self.request.user
        profile = getattr(user, 'profile', None)
        cart = self.request.session.get('cart', {})

        order = Order.objects.create(
            user=user,
            profile=profile,
            country=form.cleaned_data['country'],
            full_name=form.cleaned_data['full_name'],
            postal_code=form.cleaned_data['postal_code'],
            city=form.cleaned_data['city'],
            email=form.cleaned_data['email'],
            phone_number=form.cleaned_data['phone_number'],
            shipping_address=form.cleaned_data['shipping_address'],
            total_price=sum(item['total_price'] for item in cart.values())
        )

        for item in cart.values():
            product = get_object_or_404(Product, pk=item['pk'])

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=item['price'],
                size=item.get('size', '')
            )

        self.request.session['cart'] = {}
        self.request.session.modified = True

        return super().form_valid(form)


class ClearCartView(View):
    def post(self, request):
        request.session['cart'] = {}
        request.session.modified = True
        return redirect('cart-view')

class CheckoutView(FormView):
    template_name = 'credit-card.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('home-view')


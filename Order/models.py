from django.contrib.auth.models import User
from django.db import models
from Accounts.models import Profile
from Accounts.validators import validate_email
from Order.validators import validate_phone_number
from Shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=100)
    full_name = models.CharField()
    postal_code = models.IntegerField(max_length=10)
    city = models.CharField()
    email = models.CharField(validators=[validate_email])
    phone_number = models.IntegerField(max_length=15, validators=[validate_phone_number])
    shipping_address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20, choices=Product.SIZE_CHOICES, null=True, blank=True)



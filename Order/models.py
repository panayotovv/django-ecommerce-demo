from django.contrib.auth.models import User
from django.db import models
from Accounts.models import Profile


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
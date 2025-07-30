from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('women', 'Women'),
        ('men', 'Men'),
        ('equipment', 'Equipment'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class ItemImages(models.Model):
    image_url = models.URLField()
    item = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='item_images')


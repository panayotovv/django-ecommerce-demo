from django.db import models

class Programs(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    image_url = models.URLField()
    image_banner = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
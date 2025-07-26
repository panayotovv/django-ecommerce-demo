from django.db import models

class BaseShop(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class WomenShop(BaseShop):
    pass

class ManShop(BaseShop):
    pass

class EquipmentShop(BaseShop):
    pass

class ItemImages(models.Model):
    image_url = models.URLField()
    item = models.ForeignKey(to=WomenShop, on_delete=models.CASCADE, related_name='item_images')

class ItemImagesMan(models.Model):
    image_url = models.URLField()
    item = models.ForeignKey(to=ManShop, on_delete=models.CASCADE, related_name='item_images_man')

class ItemImagesEq(models.Model):
    image_url = models.URLField()
    item = models.ForeignKey(to=EquipmentShop, on_delete=models.CASCADE, related_name='item_images_eq')

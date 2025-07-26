from django.contrib import admin
from Shop.models import WomenShop, ManShop, EquipmentShop


@admin.register(WomenShop)
class WomenShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'price']

@admin.register(ManShop)
class ManShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'price']

@admin.register(EquipmentShop)
class EquipmentShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'price']



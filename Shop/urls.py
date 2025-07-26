from django.urls import path
from Common.views import ShopView
from Shop.views import WomenShopView, WomenDetailView, ManShopView, ManDetailView, EquipmentShopView, \
    EquipmentDetailView

urlpatterns = [
    path('', ShopView.as_view(), name='shop-view'),
    path('women/', WomenShopView.as_view(), name='women-shop'),
    path('women/<int:pk>/', WomenDetailView.as_view(), name='women-detail'),
    path('men/', ManShopView.as_view(), name='man-shop'),
    path('men/<int:pk>/', ManDetailView.as_view(), name='man-detail'),
    path('equipment/', EquipmentShopView.as_view(), name='equipment-shop'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
]
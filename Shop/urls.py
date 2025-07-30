from django.urls import path
from Common.views import ShopView
from Shop.views import ProductDetailView, ShopCategoryView

urlpatterns = [
    path('', ShopView.as_view(), name='shop-view'),
    path('<str:category>/<int:pk>/', ProductDetailView.as_view(), name='item-detail'),
    path('<str:category>/', ShopCategoryView.as_view(), name='category-shop'),
]
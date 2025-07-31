from django.urls import path
from Common.views import HomeView, AboutView, SupportView
from Order.views import AddToCartView
from Shop.views import ProductCreateView, ProductDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('about/', AboutView.as_view(), name='about-view'),
    path('support/', SupportView.as_view(), name='support-view'),
    path('add-to-cart/<str:model_name>/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('add-item/', ProductCreateView.as_view(), name='add-item'),
    path('delete-item/<int:pk>', ProductDeleteView.as_view(), name='delete-item')
]
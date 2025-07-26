from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Common.urls')),
    path('plans/', include('Programs.urls')),
    path('shop/', include('Shop.urls')),
    path('', include('Accounts.urls')),
    path('', include('Order.urls')),
]

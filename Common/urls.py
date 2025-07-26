from django.urls import path, include
from Common.views import HomeView, AboutView, SupportView

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('about/', AboutView.as_view(), name='about-view'),
    path('support/', SupportView.as_view(), name='support-view'),
]
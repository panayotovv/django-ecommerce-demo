from django.urls import path
from Accounts.views import RegisterView, CustomLoginView, ProfileDetailView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from Accounts.forms import LoginForm, RegisterForm
from Order.models import Order


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home-view')

class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home-view')


class ProfileDetailView(DetailView):
    template_name = 'profile-page.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['orders'] = Order.objects.filter(user=user)
        context['user'] = user
        return context






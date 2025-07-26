from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from Accounts.forms import LoginForm, RegisterForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home-view')

class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class BaseProfileDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['user'] = self.request.user
        return context

class ProfileDetailNoOrdersView(BaseProfileDetailView):
    template_name = 'profile-page-no-orders.html'

class ProfileDetailView(BaseProfileDetailView):
    template_name = 'profile-page-orders.html'




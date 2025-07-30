from django.views.generic import TemplateView, ListView
from Programs.models import Programs
from Shop.models import Product
import random

class HomeView(ListView):
    template_name = 'nav/home.html'
    model = Product
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_three_women'] = Product.objects.all().filter(category='women')[3:]
        context['first_three_man'] = Product.objects.all().filter(category='men')[3:]
        context['first_three_eq'] = Product.objects.all().filter(category='equipment')[3:]
        context['user'] = self.request.user
        return context


class ProgramsView(ListView):
    template_name = 'nav/plans.html'
    context_object_name = 'items'
    model = Programs

class AboutView(TemplateView):
    template_name = 'nav/about.html'

class ShopView(ListView):
    template_name = 'nav/shop.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_obj_women'] = random.choice(Product.objects.all().filter(category='women'))
        context['random_obj_man'] = random.choice(Product.objects.all().filter(category='men'))
        context['random_obj_eq'] = random.choice(Product.objects.all().filter(category='equipment'))
        return context


class SupportView(TemplateView):
    template_name = 'nav/support.html'

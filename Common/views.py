from django.views.generic import TemplateView, ListView
from Programs.models import Programs
from Shop.models import WomenShop, ManShop, EquipmentShop
import random

class HomeView(ListView):
    template_name = 'nav/home.html'
    model = WomenShop
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_three_women'] = WomenShop.objects.all()[3:]
        context['first_three_man'] = ManShop.objects.all()[3:]
        context['first_three_eq'] = EquipmentShop.objects.all()[3:]
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
    model = ManShop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_obj_women'] = random.choice(WomenShop.objects.all())
        context['random_obj_man'] = random.choice(ManShop.objects.all())
        context['random_obj_eq'] = random.choice(EquipmentShop.objects.all())
        return context


class SupportView(TemplateView):
    template_name = 'nav/support.html'

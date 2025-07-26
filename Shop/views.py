from django.views.generic import ListView, DetailView
from Shop.models import WomenShop, ManShop, EquipmentShop


class BaseDetailView(DetailView):
    template_name = 'item-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        return context


class WomenDetailView(BaseDetailView):
    model = WomenShop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        item = self.object
        context['images'] = item.item_images.all()
        return context


class ManDetailView(BaseDetailView):
    model = ManShop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        item = self.object
        context['images'] = item.item_images_man.all()
        return context

class EquipmentDetailView(BaseDetailView):
    model = EquipmentShop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        item = self.object
        context['images'] = item.item_images_eq.all()
        return context


class WomenShopView(ListView):
    template_name = 'women-shop.html'
    context_object_name = 'items'
    model = WomenShop

class ManShopView(ListView):
    template_name = 'men-shop.html'
    context_object_name = 'items'
    model = ManShop

class EquipmentShopView(ListView):
    template_name = 'equipment-shop.html'
    context_object_name = 'items'
    model = EquipmentShop









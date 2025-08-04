from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from Common.forms import CreateProduct
from Shop.models import Product

class ProductDetailView(DetailView):
    template_name = 'item-details.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['category'] = self.object.category

        item = self.object
        context['images'] = item.item_images.all()
        return context


class ShopCategoryView(ListView):
    model = Product
    template_name = 'shop-category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category')
        if category_name != 'equipment':
            context['category_name'] = f"{category_name}" + "'s Apparel"
        else:
            context['category_name'] = category_name

        return context

class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'add-item.html'
    model = Product
    form_class = CreateProduct
    success_url = reverse_lazy('shop-view')
    permission_required = 'Shop.create_Product'



class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('shop-view')
    permission_required = 'Shop.delete_Product'








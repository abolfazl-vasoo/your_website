from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product, ProductCategory


# Create your views here.

# def shop(request):
#     return render(request, 'shop/shop.html')

class ProductListView(ListView):
    template_name = 'shop/shop.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query





def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'shop/components/product_categories_component.html', context)
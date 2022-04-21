from django.shortcuts import render
from .models import GalleryImage, Product
from app_home.models import Setting
# Create your views here.


def ShopView(request):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    context = {
        'products':products,
        'setting':setting,
    }
    return render(request, 'product/shop.html', context)


def ProductDetailView(request, slug):
    you_may_like_products = Product.objects.all().order_by('?')[:6]  # random 6
    product = Product.objects.get(slug=slug)
    images = GalleryImage.objects.filter(product_id=product.id)
    context = {
        'product': product,
        'you_may_like_products': you_may_like_products,
        'images': images,
    }
    return render(request, 'product/product-detail.html', context)
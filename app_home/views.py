from django.shortcuts import render
from .models import Setting, FAQ
from app_product.models import Product
from app_product.models import Category
# Create your views here.


def IndexView(request):
    setting = Setting.objects.get(pk=1)
    top_categories = Category.objects.all().order_by('-id')[:3]  # first 3 category
    HomeSliders = Product.objects.all().order_by('?')[:4]  # random 4
    featured_products = Product.objects.all().order_by('?')[:6]  # random 6
    latest_collections = Product.objects.all().order_by('-id')[:7]  # last 7 
    context = {
        'setting': setting,
        'top_categories': top_categories,
        'HomeSliders': HomeSliders,
        'featured_products': featured_products,
        'latest_collections': latest_collections,
    }
    return render(request, 'home/index.html', context)


def AboutusView(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting,
    }
    return render(request, 'home/about.html', context)

def CategoryView(request, id, slug):
    products = Product.objects.filter(category_id=id)
    catdata = Category.objects.get(pk=id)
    you_may_like_products = Product.objects.all().order_by('?')[:6]  # random 6
    context = {
        'products': products,
        'you_may_like_products': you_may_like_products,
        'catdata': catdata,
    }
    return render(request, 'home/category_products.html', context)

def faqView(request):
    setting = Setting.objects.get(pk=1)
    faqs = FAQ.objects.filter(status=True).order_by("ordernumber")
    context = {
        'faqs': faqs,
        'setting': setting,
    }
    return render(request, 'home/faq.html', context)

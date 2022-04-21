from django import template
from app_product.models import Category, Product
register = template.Library()
@register.simple_tag
def CategoryList():
    return Category.objects.all()
@register.simple_tag
def ProductList():
    return Product.objects.all()

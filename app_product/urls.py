from django.urls import path


from . import views
app_name = 'Product'

urlpatterns = [
    path('', views.ShopView, name="ShopView"),
    path('<slug:slug>/', views.ProductDetailView, name="ProductDetailView"),
]

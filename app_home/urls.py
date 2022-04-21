from django.urls import path




from . import views
app_name = 'Home'

urlpatterns = [
    path('', views.IndexView, name="IndexView"),
    path('about-us/', views.AboutusView, name="AboutusView"),
    path('category/<int:id>/<slug:slug>', views.CategoryView, name="CategoryView"),
    path('faq/', views.faqView, name="faqView"),
]

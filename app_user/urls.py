from django.urls import path


from . import views

app_name = 'App_User'

urlpatterns = [
    path('sign-up/', views.SignUpView, name="SignUpView"),
    path('login/', views.LoginView, name="LoginView"),
    path('', views.ProfileView, name="ProfileView"),
]

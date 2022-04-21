from django.shortcuts import render
# Create your views here.

def LoginView(request):
    return render(request, 'user/login.html')
def SignUpView(request):
    return render(request, 'user/signup.html')
def ProfileView(request):
    return render(request, 'user/profile.html')

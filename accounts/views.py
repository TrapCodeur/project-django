from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate 
from django.contrib import messages



# Create your views here.
User = get_user_model()
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe deja. Veillez en choisir un autre")
            return redirect('verify')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        return render(request, "accounts\\signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('verification')
            
    return render(request, "accounts\\login.html")

def logout_user(request):
    logout(request)
    return redirect('index')


def verify(request):
    return render(request, "accounts\\verify.html")

def verification(request):
    return render(request, "accounts\\verification.html")
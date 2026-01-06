from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def salam(request):
    return HttpResponse("<h1 align='center'>Selamat Belajar Django</h1>")


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def form_pemesanan(request):
    return render(request, 'form_pemesanan.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('login')

    return render(request, 'signup.html')
